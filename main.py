import speech_recognition as sr
import aiml
import pyttsx3
import config

def tts(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('rate', config.speechRate) 
    engine.setProperty('volume', config.speechVolume) 
    engine.setProperty('voice', voices[config.speechGender].id)
    print(f"Output: {text}")
    engine.say(text)
    engine.runAndWait()

def runBot(say_IN):
    say = say_IN
    response = kernel.respond(say)
    tts(response)

def runAI():
    while True:
        r = sr.Recognizer()
        r.pause_threshold = 3
        r.non_speaking_duration = 3

        with sr.Microphone() as source:
            print("Speak now:")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            runBot(text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said")
        except sr.RequestError as e:
            print(f"Error making request: {e}")

if(__name__=="__main__"):
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("LOAD AIML B")
    runAI()
