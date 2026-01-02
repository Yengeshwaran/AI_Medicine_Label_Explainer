# 💊 AI Medicine Label Explainer (Medico)

**A Local, Privacy-First AI Assistant for Elderly Users**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![AI](https://img.shields.io/badge/AI-Ollama%20%7C%20Tesseract-green)

## 📖 Project Overview
The **AI Medicine Label Explainer** is a student-level project designed to help elderly users or people with low literacy understand complex medicine labels. 
It takes a photo of a medicine bottle, reads the text using **OCR (Optical Character Recognition)**, and uses a **Local LLM (Large Language Model)** to explain it in simple, plain English or Tamil.

**Key Goals:**
- **Simplicity**: No complex medical jargon.
- **Privacy**: Runs 100% offline. No health data is sent to the cloud.
- **Accessibility**: Large fonts, simple UI, and **Text-to-Speech (TTS)** support.

---

## 🛠️ Technology Stack
This project uses **Free and Open-Source** tools:
- **Language**: Python
- **Frontend**: Streamlit
- **OCR Engine**: Tesseract-OCR (via `pytesseract`)
- **AI Model**: Ollama (running `mistral` or `llama3`)
- **Text-to-Speech**: `pyttsx3` (Offline)

---

## 📂 Project Structure
- `app.py`: The main application file containing the UI and logic.
- `ocr_module.py`: Handles image processing and text extraction.
- `simplify_module.py`: Connects to the local AI model to simplify text.
- `tts_module.py`: Converts the simplified text into audio.
- `demo_module.py`: Manages the built-in demo mode using sample assets.
- `assets/`: Contains sample images for testing.

---

## 🚀 Installation Guide

### 1. Prerequisites
Ensure you have **Python** installed. You also need these two external tools:

1.  **Tesseract OCR**:
    - Download and install from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
    - **Important**: Add the installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your System **PATH** variable.

2.  **Ollama**:
    - Download from [ollama.com](https://ollama.com).
    - Install and run `ollama serve` in a terminal window.
    - Pull the model we use:
      ```bash
      ollama pull mistral
      ```

### 2. Install Python Dependencies
Open your terminal in this project folder and run:
```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ How to Run
1.  Make sure **Ollama** is running in a separate terminal (`ollama serve`).
2.  Run the application:
    ```bash
    streamlit run app.py
    ```
3.  The app will open in your browser (usually at `http://localhost:8501`).

---

## 🎮 How to Use
1.  **Select Language**: Choose **English** or **Tamil** from the top menu.
2.  **Try Demo**: Click the **"Try Demo"** tab and hit **"Load & Run Demo Image"**. The app will automatically process the sample medicine label.
3.  **Upload Your Own**: detailed Check the **"Upload Image"** tab to upload a photo (`.jpg`, `.png`) of any medicine label.
4.  **Read Out Loud**: Scroll to the bottom and click the **"🔊 Read Out Loud"** button to hear the explanation.

---

## ⚠️ Safety Disclaimer
**This application is for educational purposes only.**
- It explains only the text written on the label.
- It **does not** provide medical advice, diagnosis, or treatment.
- Always consult a doctor or pharmacist for medical concerns.
