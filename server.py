"""This app meters the emotion of the sentences"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Function to call the emotion detector"""    
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    if dominant is None:
        return "<b> Invalid text! Please try again</b>"

    return f"For the given statement, the system response is \
    'anger': {anger}, 'disgust': {disgust}, \
    'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. The dominant emotion is <b>{dominant}</b>."

@app.route("/")
def render_index_page():
    """Main function"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
