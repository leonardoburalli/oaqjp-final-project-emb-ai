from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def em_detector():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
    else:
        emotion_values = [f"'{key}': {value}" for key, 
        value in response.items() if key not in ("sadness" ,"dominant_emotion")]

        result_string = f"For the given statement, the system response is {', '.join(emotion_values)}" \
        f" and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
        return result_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444)