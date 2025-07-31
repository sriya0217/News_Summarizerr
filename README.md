# News_Summarizerr Web App
An intelligent Flask-based web application that automatically summarizes long news articles, documents, and even image-based content using AI-powered NLP and OCR technologies.This News Summarizer web application was developed as a practical demonstration of integrating Natural Language Processing (NLP) with OCR technology in a modern, user-friendly web interface. It enables users to quickly summarize long-form content from various sources such as pasted text, documents, or images. The app is built using Python and Flask, with key support from Tesseract OCR and Transformer-based models for text summarization. Designed with a sleek, glassmorphic UI, it aims to make information consumption faster and more efficient. Whether for research, journalism, or education, this project offers a smart solution to save time and improve comprehension.

✨ Features

📝 Text Input: Paste or type any article or paragraph for summarization.
📁 File Upload: Supports .txt, .pdf, .docx, and .jpg/.png image files.
📷 OCR Support: Extracts text from image files using Tesseract OCR.
🧠 AI-Powered Summary: Uses Hugging Face transformers to generate meaningful summaries.
🎨 Modern UI: Beautiful, responsive design with glassmorphic styling using pure HTML & CSS.
⚡ Fast & Lightweight: Built on Flask – minimal yet powerful.
🛠️ Tech Stack

💻 Backend

Python
Flask
pytesseract – for OCR
transformers – for summarization
PyPDF2 – PDF reading
python-docx – DOCX parsing

🌐 Frontend

HTML5 + Internal CSS
Custom styling with background image and glassmorphic UI
Responsive for desktop & mobile

🚀 How It Works


User Input:

Paste text or upload a file.

Processing:

Text is extracted based on file type (image, PDF, Word, or text).
(Optional) Text is translated to English.
Text is passed to a transformer summarizer model.

Output:

A clear, concise summary is shown to the user.
