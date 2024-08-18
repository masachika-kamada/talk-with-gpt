import azure.cognitiveservices.speech as speechsdk
import os


def synthesize_speech_to_file(text, filename):
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), region=os.getenv("REGION"))
    speech_config.speech_synthesis_voice_name = "ja-JP-DaichiNeural"
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
