import os
import wave
import json
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from backend.config import UPLOAD_DIR

# Load offline STT model (download Vosk model separately, e.g. "vosk-model-small-en-us-0.15")
MODEL_PATH = "vosk-model-small-en-us-0.15"
if os.path.exists(MODEL_PATH):
    stt_model = Model(MODEL_PATH)
else:
    stt_model = None


def speech_to_text(file_path: str):
    if not stt_model:
        return "STT model not found."

    audio = AudioSegment.from_file(file_path)
    wav_path = os.path.join(UPLOAD_DIR, "temp.wav")
    audio.export(wav_path, format="wav")

    wf = wave.open(wav_path, "rb")
    rec = KaldiRecognizer(stt_model, wf.getframerate())
    rec.SetWords(True)

    text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text += result.get("text", "") + " "
    wf.close()

    return text.strip()
