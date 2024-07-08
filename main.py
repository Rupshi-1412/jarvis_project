"""This project is a voice-activated assistant using various 
Python libraries to provide interactive features such as
voice recognition, text-to-speech, web browsing, telling jokes, and many more.
Below is a brief documentation of the project."""


import pyttsx3 as p             # Text-to-speech conversion library.
import speech_recognition as sr     # Library for performing speech recognition.
import pyjokes              # Library to fetch jokes.
import pyaudio              # Used to capture and play audio.
import webbrowser           # Library to open web pages.
import datetime             # Module to handle date and time operations.
import setuptools           # Used for packaging Python projects (imported but not used directly in the code).
import musicLibrary         # Custom module assumed to hold a dictionary of songs and their respective URLs.
import pyautogui            # Library for GUI automation, used here for taking screenshots.
import time                 # Module for handling time-related functions.
import pyscreeze            # Library for image manipulation (imported but not used directly in the code).




"""Text-to-Speech Engine Initialization:"""

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


"""Speech Function: Converts text to speech."""

def speech(text) :

    engine.say(text)
    engine.runAndWait()
    

"""Speech-to-Text Function: Converts speech to text 
using Google Speech Recognition API."""

def speech_to_text() :

    recognizer = sr.Recognizer()     # creating the object Recognizer class

    with sr.Microphone(device_index=1) as source :
        print("listening .....")
        recognizer.energy_threshold = 10000  # it increeases spectrum of our 
        #voice(capture low voices)
        recognizer.adjust_for_ambient_noise(source) #cancels all the 
        #noises around you
        
        text = ""
        try :
            audio = recognizer.listen(source,timeout=4,phrase_time_limit=3)  #listen to the source
            print("Recognizing .....")
            text = recognizer.recognize_google(audio).lower() #getting the audio and 
            #send it to google api to convert it into text
            print(text)
        except Exception as e :
            print("Not understanding......")
        
    
    return text


"""Main Program Flow"""

if __name__ == '__main__' :

    # Greeting :

    speech("Hey, I am your DJ assistant ,enter your name....")
    name = input("Enter your name : ")
    str = ("Hey",name,"now, tell me how can I help you?")

    speech(str)
    engine.runAndWait()

    """Continuous Listening Loop:
    The program enters a continuous loop, listening for commands and responding accordingly.
    **Voice Commands:
    1.Asking the assistant's name and age.
    2.Getting the current time and date.
    3.Opening YouTube and Google in a web browser.
    4.Telling jokes.
    5.Playing songs from a custom music library.
    6.Taking and saving screenshots.
    7.Exiting the program gracefully."""


    while True :

        data = speech_to_text()

        if "your name" in data :
            name = "My name is DJ assistant"
            speech(name)
        elif "old" in data :
            old = "I am one year old"
            speech(old)
        elif "time" in data :
            time = datetime.datetime.now().strftime("%I%M%p")  # I gives hours, M gives minutes and ,p gives am or pm
            speech(time)
        elif "youtube" in data :
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data :
            jokes = pyjokes.get_joke(language="en",category="neutral")
            speech(jokes)
            print(jokes)
        elif "date" in data :
            date_1= datetime.datetime.now().date()
            speech(date_1)
        elif "google" in data :
            webbrowser.open("https://www.google.co.in/")
        elif "play" in data:
            song = data.split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
        elif "screen" in data :
            speech("tell me the name of your screenshot file ")
            name_ss = speech_to_text()
            #name_ss = 'image'
            speech("hold the screen for few seconds,I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f'{name_ss}.png')
            speech("I am done.Screenshot is saved in our main folder ")

        elif "exit" in data :
            speech("Thank you")
            break
        

print("thanks")

"""Note
Ensure the following:

** Microphone is properly configured and connected.
** Google Speech Recognition API has internet access.
** Update the musicLibrary with your desired song links.
** Necessary permissions are granted for accessing the microphone and saving files."""