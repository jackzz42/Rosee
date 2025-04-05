import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("voice", "english+f4")
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return ""

def wait_for_wake_word(wake_word="hey rosee"):
    while True:
        print("Waiting for wake word...")
        command = listen().lower()
        if wake_word in command:
            print("Wake word detected!")
            speak("Yes?")
            break
