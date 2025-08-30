import pyttsx3
import speech_recognition as sr
import google.generativeai as genai

# --- Configuration ---
genai.configure(api_key="your_api_key_here")
model = genai.GenerativeModel("gemini-pro")

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as src:
            print("Listening...")
            audio = recognizer.listen(src)

        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Generate AI response
        response = model.generate_content(text)
        print("Assistant:", response.text)

        # Speak response
        speak(response.text)

    except sr.UnknownValueError:
        print("Sorry, I didn’t catch that.")
    except sr.RequestError:
        print("Speech recognition service unavailable.")
    except Exception as e:
        print("Error:", e)
