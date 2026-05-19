"""
Server module for the Emotion Detection application.
Executes a Flask server to host the web interface and API endpoint.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Disable invalid-name warning since 'app' is the standard Flask instance variable convention
# pylint: disable=invalid-name
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the input text for emotions and returns a formatted response string.
    Handles invalid or blank entries gracefully by verifying the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index HTML template for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    