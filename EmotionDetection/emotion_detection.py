import requests, json

def emotion_detector(text_to_analyze):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions = {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}
        refScore = 0
        refEmotion = 'na'
        for k,v in emotions.items():
            if v>refScore:
                refScore=v
                refEmotion=k
        emotions["dominant_emotion"] = refEmotion

    # If the response status code is 500 or 400, set emotions to None
    elif (response.status_code == 400) or (response.status_code == 500) :
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        emotions = {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}
        dominant = None
        emotions["dominant_emotion"] = dominant

    return emotions

