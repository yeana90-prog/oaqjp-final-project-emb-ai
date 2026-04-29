"""Flask server for Emotion Detection application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("EmotionDetection")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
