# Mr Techno
import speech_recognition
import speech_recognition as sr
import pyttsx
from time import ctime
import time
import os
from gtts import gTTS
import sqlite3


conn = sqlite3.connect('Photogeniks.db')
#speech_engine = pyttsx.init('sapi5') 
#speech_engine.setProperty('rate', 150)


def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		return recognizer.recognize_sphinx(audio)
		# or: return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""
 
def photoi(data):

    if "what are we going to eat" in data:
        speak("There is currently ,raw food , Some sauges in the fridge,rice, chicken. What is your choice")
    if "what is your name" in data:
        speak("My name is Photo eye ,My ,creator, is ,Mr techno")


    if "how many people are in the room" in data:
        speak("There 2 people currently, Mr yamii and Mr techno")
        #print("My name is Photo eye ,My creator is Mr techno")
    if "what is your purpose" in data:
        speak("My purpose is to capture images and Carry out The Task of Attendance")
        
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
    if "how many students are there" in data:

        print "Opened database successfully";
        cursor = conn.execute("SELECT count(*) FROM People;")

        rows = cursor.fetchall()


        for row in rows:
            print(row)
            speak("There are")
            speak(row)
            speak("Students")
    if "search for Sarah" in data:
        print "Opened database successfully";
        cursor = conn.execute("SELECT *FROM People where Name = 'Sarah'")

        rows = cursor.fetchall()

        for row in rows:
            print(row)
            speak("Description is")
            speak(row)






			




		
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on There, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hi There, what can I do for you?"+listen())
while 1:
    data = recordAudio()
    photoi(data)
