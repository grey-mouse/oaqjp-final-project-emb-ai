import json
import requests

def emotion_detector(text_to_analyze: str) -> str:
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json = input_json, headers = header, timeout = 5)
    response_json = json.loads(response.text)

    analysis = {}
    for emotion, score in response_json["emotionPredictions"][0]["emotion"].items():
        analysis[emotion] = score
    analysis["dominant_emotion"] = max(analysis, key = analysis.get)

    return analysis
