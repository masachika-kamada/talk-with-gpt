import os

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv


def initialize_speech_config():
    load_dotenv()
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region=os.getenv("REGION"))
    speech_config.speech_synthesis_voice_name = "ja-JP-DaichiNeural"
    return speech_config


def synthesize_speech_to_file(text, filename):
    speech_config = initialize_speech_config()
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("音声合成が完了しました。ファイルに保存されました。")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("音声合成がキャンセルされました: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("エラーの詳細: {}".format(cancellation_details.error_details))


if __name__ == "__main__":
    text = "無添加のシャボン玉石鹸ならもう安心天然の保湿成分が含まれるため、肌に潤いを与え、健やかに保ちます。お肌のことでお悩みの方はぜひ一度無添加シャボン玉石鹸をお試しください。お求めは0120005595まで。"
    filename = "output.mp3"
    synthesize_speech_to_file(text, filename)
