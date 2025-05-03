from faster_whisper import WhisperModel

model = WhisperModel("base")

def transcribe_audio(file):
    segments, _ = model.transcribe(file, beam_size=5)
    text = " ".join([segment.text for segment in segments])
    return text
