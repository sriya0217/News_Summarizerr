from flask import Flask, render_template, request
from PIL import Image
import pytesseract
from PyPDF2 import PdfReader
from transformers import pipeline
from deep_translator import GoogleTranslator
import os
import docx
import re

# Initialize Flask app
app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sriya_d6nsi2c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=130, min_length=30):
    if not text.strip():
        return "No content to summarize."
    try:
        result = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return "Summarization failed."

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    uploaded_filename = ""

    if request.method == "POST":
        text = request.form.get("article", "")
        uploaded_file = request.files.get("file")

        if uploaded_file:
            uploaded_filename = uploaded_file.filename
            ext = uploaded_filename.rsplit('.', 1)[-1].lower()

            # Handle image OCR (English only)
            if ext in ['png', 'jpg', 'jpeg']:
                image = Image.open(uploaded_file)
                text = pytesseract.image_to_string(image, lang='eng')

            # Handle PDF
            elif ext == 'pdf':
                reader = PdfReader(uploaded_file)
                text = "".join(page.extract_text() for page in reader.pages if page.extract_text())

            # Handle DOCX
            elif ext == 'docx':
                doc = docx.Document(uploaded_file)
                text = "\n".join([para.text for para in doc.paragraphs])

            # Handle TXT
            elif ext == 'txt':
                text = uploaded_file.read().decode('utf-8')

        # Translate to English if needed
        if text.strip():
            try:
                text = GoogleTranslator(source='auto', target='en').translate(text)
            except:
                pass

            # Clean and normalize
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"([.?!])", r"\1 ", text)

            summary = summarize_text(text)

    return render_template("index.html", summary=summary, filename=uploaded_filename)

if __name__ == "__main__":
    app.run(debug=True)
