from fastapi import FastAPI, UploadFile
from utils.scam_detection import detect_scam
from utils.url_checker import check_url
from utils.speech_to_text import transcribe_audio
from utils.text_to_speech import speak_result

app = FastAPI()

@app.post("/analyze-text/")
async def analyze_text(data: dict):
    result = detect_scam(data["text"], data["lang"])
    return result

@app.post("/check-url/")
async def check_url_endpoint(data: dict):
    return check_url(data["url"])

@app.post("/analyze-audio/")
async def analyze_audio(file: UploadFile):
    text = transcribe_audio(file.file)
    result = detect_scam(text)
    return result

@app.post("/speak/")
async def speak(data: dict):
    audio_path = speak_result(data["text"], data["lang"])
    return {"audio_path": audio_path}