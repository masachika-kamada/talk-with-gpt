import threading
import tkinter as tk
from tkinter import filedialog

from dotenv import load_dotenv

from src.chat import get_ai_response
from src.play_audio import play_audio
from src.record import Recorder
from src.stt import speech_to_text
from src.tts import synthesize_speech_to_file

load_dotenv()


class SpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("音声アプリ")

        self.start_button = tk.Button(root, text="発話開始", command=self.start_recording)
        self.start_button.grid(row=0, column=0)

        self.stop_button = tk.Button(root, text="発話終了", command=self.stop_recording)
        self.stop_button.grid(row=0, column=1)

        self.text_area = tk.Text(root)
        self.text_area.grid(row=1, column=0, columnspan=2)

        self.audio_file = "recorded_audio.wav"
        self.output_file = "output.mp3"
        self.recorder = Recorder(self.audio_file)

    def start_recording(self):
        self.recorder.start_recording()

    def stop_recording(self):
        self.recorder.stop_recording()
        threading.Thread(target=self.process_audio).start()

    def process_audio(self):
        # 文字起こし
        transcription = speech_to_text(self.audio_file)
        self.text_area.insert(tk.END, f"文字起こし: {transcription}\n")

        # AI応答
        ai_response = get_ai_response(transcription)
        self.text_area.insert(tk.END, f"AI応答: {ai_response}\n")

        # 音声合成
        synthesize_speech_to_file(ai_response, self.output_file)

        # 音声再生
        play_audio(self.output_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechApp(root)
    root.mainloop()
