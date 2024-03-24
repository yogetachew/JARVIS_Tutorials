"""
    name: javis_wikipedia.py 
    Author: Yonatan Getachew 
    Created: 3/24/2024
""" 

# pip install wikipedia and pyttsx3
import pyttsx3
import wikipedia
import speech_recognition as sr

# Initialize the text to speech engine
engine = pyttsx3.init()

# define speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# get the summary from wikipesia
# used the perivous code form wikipedia_1.py file 
# and added the error message
def get_wikipedia_summary(search_terms):
    try:
        summary = wikipedia.summary(search_terms)
        return summary
    except wikipedia.exceptions.PageError:
        return "Sorry, no information"
    except wikipedia.exceptions.DisambiguationError:
        return "Multiple matches found. Please be more specific."

# TODO: get command from the user
def get_command():
    """Function to get a command from the user using speech recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(command)
        return command
    except sr.UnknownValueError:
        print("Sorry, try speaking again")
        return ""
    except sr.RequestError:
        print("Sorry, speech service is down.")
        return ""

# TODO: Main 
# list down the option
def main():
    speak("Hello! How can I assist you today?")
    while True:
        speak("Please choose a command:")
        print("1. Wikipedia")
        print("2. Exit")
        
        # TODO: Ask user for a choice
        choice = get_command()
        
        # TODO: list the options wikipedia or exit
        if "wikipedia" in choice:
            speak("what question do you have today?")
            command = get_command()
            result = get_wikipedia_summary(command)
            speak("Here is the answer from Wikipedia:")
            speak(result)
            print("Wikipedia Answer:")
            print(result)
        elif "exit" in choice:
            speak("Exiting the program.")
            break
        else:
            speak("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
