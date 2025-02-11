import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("say something")
            audio  = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print(f"The text: {text}")
    except:
        print("Couldnt understand")
        r = sr.Recognizer()
        continue





