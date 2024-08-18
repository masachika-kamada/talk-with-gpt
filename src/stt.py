import json
import os

import requests


def speech_to_text(file_path):
    subscription_key = os.getenv("SUBSCRIPTION_KEY")
    region = os.getenv("REGION")
    api_url = f"https://{region}.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-05-15-preview"

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
    return response.json()['combinedPhrases'][0]['text']
