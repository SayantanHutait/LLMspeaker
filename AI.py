import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Set up Gemini API Key
genai.configure(api_key="API")

# Initialize Speech Recognizer
r = sr.Recognizer()
engine = pyttsx3.init()

while True:
    try:
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)
            text = r.recognize_google(audio).lower()

            print(f"You said: {text}")

            # Get AI Response from Gemini
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(text)
            AI_reply = response.text

            print(f"AI says: {response.text}")

            engine.say(AI_reply)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Couldn't understand, try again...")
    except Exception as e:
        print(f"Error: {e}")
