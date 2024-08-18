#!/bin/bash

# サンプル音声ファイルをダウンロード
if [ ! -f sample_audio.mp3 ]; then
  curl -o sample_audio.mp3 https://pro-video.jp/voice/announce/mp3/001-sibutomo.mp3
fi

# .envファイルを読み込む
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# cURLコマンドを実行
curl --location "https://${REGION}.api.cognitive.microsoft.com/speechtotext/transcriptions:transcribe?api-version=2024-05-15-preview" \
--header "Content-Type: multipart/form-data" \
--header "Accept: application/json" \
--header "Ocp-Apim-Subscription-Key: ${SUBSCRIPTION_KEY}" \
--form "audio=@sample_audio.mp3" \
--form 'definition={"locales":["ja-JP"],"profanityFilterMode":"Masked","channels":[0]}'
