from flask import Flask, request, jsonify, render_template, send_from_directory
from utils.scam_detection import detect_scam
from utils.speech_to_text import transcribe_audio
from utils.text_to_speech import speak_result
from utils.url_checker import check_url
import os

app = Flask(__name__)

# Serve the main HTML page
@app.route("/")
def index():
    return render_template("index.html")

# Route to analyze text for scams
@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    data = request.json
    result = detect_scam(data["text"], data.get("lang", "en"))
    return jsonify(result)

# Route to check if a URL is safe
@app.route("/check-url", methods=["POST"])
def check_url_api():
    data = request.json
    result = check_url(data["url"])
    return jsonify(result)

# Route to analyze uploaded audio for scam
@app.route("/analyze-audio", methods=["POST"])
def analyze_audio():
    file = request.files['file']
    text = transcribe_audio(file)
    result = detect_scam(text)
    return jsonify(result)

# Route to convert text to speech (TTS)
@app.route("/speak", methods=["POST"])
def speak():
    data = request.json
    path = speak_result(data["text"], data.get("lang", "en"))
    filename = os.path.basename(path)
    return jsonify({"audio_path": f"/static/{filename}"})

# Route to serve the generated audio file
@app.route('/static/<path:filename>')
def serve_audio(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
