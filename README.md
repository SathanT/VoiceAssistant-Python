# VoiceAssistant-Python

A Python-based AI Voice Assistant that uses **speech recognition**, **text-to-speech (TTS)**, and **Google Gemini (Generative AI)** to listen, understand, and respond to user commands in real-time.

---

## ✨ Features
- 🎙️ Convert speech to text using **Google Speech Recognition**  
- 🗣️ Speak responses with **pyttsx3** text-to-speech engine  
- 🤖 AI-powered replies with **Google Generative AI (Gemini)**  
- ⚡ Continuous listening loop for hands-free interaction  

---

## 📂 Project Structure
```
VoiceAssistant-Python/
│── main.py               # Main script
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── .gitignore            # Prevents API keys & cache from uploading
```

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/VoiceAssistant-Python.git
   cd VoiceAssistant-Python
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 API Key Setup

⚠️ **Important:** Keep your Gemini API key private. Do **not** hardcode it into your code.

1. Create a `.env` file:
   ```
   API_KEY=your_gemini_api_key_here
   ```

2. Update your script to load it:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   genai.configure(api_key=os.getenv("API_KEY"))
   ```

3. Add `.env` to `.gitignore` so it’s never uploaded.

---

## ▶️ Usage

Run the assistant:
```bash
python main.py
```

Then just **speak your query** (e.g., “Tell me a joke”, “Explain OOP in Python”).  
The assistant will listen 🎙️, generate an AI response 🤖, and speak it aloud 🗣️.  

---

## 📌 Example Interaction
```
Listening...
You said: What is Python?
Assistant: Python is a versatile high-level programming language known for its readability and wide usage in AI, web development, and automation.
```

---

## 🛠️ Technologies Used
- **Python 3.x**  
- [pyttsx3](https://pypi.org/project/pyttsx3/) – Text-to-Speech  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – Speech-to-Text  
- [pyaudio](https://pypi.org/project/PyAudio/) – Microphone input  
- [google-generativeai](https://ai.google.dev/) – AI-powered responses (Gemini)  

---

## 📄 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
