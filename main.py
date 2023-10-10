import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine= pyttsx3.init()
engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty("rate",120)
try:
    with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print(command)
            if "hello" in command:
                engine.say("ahh uhh")

                engine.runAndWait()
except:
    pass