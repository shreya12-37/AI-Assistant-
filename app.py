import pyttsx3
import datetime

engine = pyttsx3.init()
# engine.say("hello everyone")
# engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 160
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello Everyone")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

#time()
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


