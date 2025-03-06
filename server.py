'''
    Initiates the application for emotions analysis to be executed over the Flask channel
    and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotions():
    '''
        This function receives the text from the HTML interface and 
        runs emotions analysis over it. 
        The output returned shows the emotions, there scores and
        the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result_string = f"For the given statement, the system response is " \
    f"'anger': {result['anger']}, " \
    f"'disgust': {result['disgust']}, " \
    f"'fear': {result['fear']}, " \
    f"'joy': {result['joy']} and " \
    f"'sadness': {result['sadness']}. " \
    f"The dominant emotion is <b>{result['dominant_emotion']}</b>."

    return result_string

@app.route("/")
def render_index_page():
    '''
        This function initiates the rendering of the main application.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
