import os
from gtts import gTTS
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "static/audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def text_to_speech(text):
    """Convert text to speech and save as an audio file"""
    tts = gTTS(text=text, lang="en")
    filename = "speech.mp3"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    tts.save(filepath)
    return filepath

@app.route("/", methods=["GET", "POST"])
def home():
    audio_file = None
    if request.method == "POST":
        text = request.form.get("text")
        audio_file = text_to_speech(text)

    return render_template("index.html", audio_file=audio_file)

if __name__ == "__main__":
    app.run(debug=True)
