import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def test_speech_to_text_api(file_path, api_url, subscription_key):
    headers = {
        "Accept": "application/json",
        "Ocp-Apim-Subscription-Key": subscription_key
    }
    definition = {
        "locales": ["ja-JP"],
        "profanityFilterMode": "Masked",
        "channels": [0]
    }
    files = {
        "audio": ("audio.wav", open(file_path, "rb")),
        "definition": (None, json.dumps(definition), "application/json")
    }

    response = requests.post(api_url, headers=headers, files=files)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()['combinedPhrases'][0]['text']}")


if __name__ == "__main__":
    file_path = "sample_audio.mp3"
    subscription_key=os.getenv("SUBSCRIPTION_KEY")
    region=os.getenv("REGION")

    api_url = f"https://{region}.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-05-15-preview"

    test_speech_to_text_api(file_path, api_url, subscription_key)
