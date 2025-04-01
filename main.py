import speech_recognition as sr
import pyttsx3
import threading
import datetime
import random
import os
import sys
import traceback
import time

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    print(f"\nACOSAR | {text}")
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        time.sleep(2)
        os.system('speak')
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language='en-us')
        os.system('hzd')
        print(f"\nYou | {query}")
        return query.lower()
    except Exception:
        return None

def process_command(command):
    if command:
        if 'you there' in command or 'you alive' in command:
            responses = ["Yes sir", "For you sir, always", "Of course sir"]
            speak(random.choice(responses))
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("The %d of %B")
            speak(f"Today's date is {current_date}")
        elif 'restart' or 'reboot' in command:
            speak("Rebooting")
            os.execv(sys.executable, ['python'] + sys.argv)
        elif 'exit' in command:
            speak("Goodbye!")
            sys.exit()

def listening_thread():
    while True:
        command = listen()
        if command:
            processing_thread = threading.Thread(target=process_command, args=(command,))
            processing_thread.start()

def main():
    if len(sys.argv) < 2:
        speak("Please provide the password as a command-line argument")
        return
    
    password = sys.argv[1]
    if password == "81321":
        speak("Access granted. Welcome sir")
        listen_thread = threading.Thread(target=listening_thread)
        listen_thread.start()
    else:
        speak("Incorrect password")

if __name__ == "__main__":
    main()