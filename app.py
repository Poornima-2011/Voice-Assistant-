import pyttsx3
import speech_recognition as sr
import webbrowser

import wikipedia
from datetime import datetime
from weather import get_weather #Import function from weather.py
from wish import wish_user  # Import function from wish.py 
from news import get_news  # Import function from news.py
from googletrans import Translator
from date import get_current_date  # Import function from date.py
from translate import translate_to_tamil  # Import function from translate.py
import os
from todo import add_task, remove_task, show_tasks
from email_sender import send_email


# Initialize the voice engine
engine = pyttsx3.init()

# Set properties for speech (rate of speech, volume)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to speak the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            speak("Sorry, there was an issue with the speech recognition service.")
            return None
        
def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is too ambiguous, here are some options: {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Sorry, I couldn't fetch information at the moment. Please try again later."



# Function to handle various commands
def handle_command(command):
    if 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
        print("opening youtube")
    
    elif "add task" in command:
        speak("What task would you like to add?")
        task = listen()
        response = add_task(task)
        speak(response)
        print(response)

    elif "remove task" in command:
        speak("Which task would you like to remove?")
        task = listen()
        response = remove_task(task)
        speak(response)
        print(response)

    elif "show tasks" in command:
        response = show_tasks()
        speak(response)
        print(response)
    
    elif 'send email' in command:
      speak("Who is the recipient?")
      to_name = listen().lower()

      email_dict = {
        # "john": "john@example.com",
        "poorni": "poorni2045@gmail.com"
        
        # "Arunehh": "arunehh30@gmail.com"
      }
      to_email = email_dict.get(to_name)
    
      if not to_email:
        speak("Sorry, I don't have that contact.")
        return  # Exit handle_command instead of using 'continue'

      speak("What is the subject?")
      subject = listen()

      speak("What should I say?")
      content = listen()

    # Replace these with your actual email and app password (use .env in production!)
      from_email = "poornimasiva20@gmail.com"
      from_password ="nvmmkhdlqnisqtjw"

      if send_email(to_email, subject, content, from_email, from_password):
          speak("Email sent successfully.")
      else:
          speak("Failed to send email.")

 
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
        print("opning Google")

    
    
    elif 'weather' in command:
        # city = "New York"  # You can ask the user for a city name or use a default one
        speak("Please tell me the name of the city you want the weather for.")
        city = listen()  # Listen for the city name
        if city:
            speak(f"Fetching weather for {city}.")
            print(f"Fetching weather for {city}...")
            weather_report = get_weather(city)  # Fetch the weather report
            print(weather_report)  # Print the weather report
            speak(weather_report)  # Read the weather report out loud
    
    elif 'news' in command:
        news_report = get_news()
        print(news_report)
        speak(news_report)
        
    elif 'play video on youtube' in command:
        speak("What video would you like to play?")
        video_query = listen()
        if video_query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={video_query}")
            speak(f"Playing {video_query} on YouTube.")
    
    elif 'hello' in command:
        greeting = wish_user()  # Call the wish_user function from wish.
        print(greeting) 
        speak(greeting)  # Greet the user
        print("How can I assist you today?")
        speak("How can I assist you today?")
    

    elif 'date' in command or 'today' in command:
        current_date = get_current_date()
        speak(f"Today's date is {current_date}.")
        print(f"Today's date is {current_date}.")
         # current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        # speak(f"Today's date is {current_date}")
    
    elif 'open spotify' in command:
        try:
            os.system("spotify")  # Ensure Spotify is installed
            speak("Opening Spotify.")
        except Exception as e:
            speak("Sorry, I couldn't open Spotify.")
            print(e)

    elif 'open notepad' in command:
        try:
            os.system("notepad")
            speak("Opening Notepad.")
        except Exception as e:
            speak("Sorry, I couldn't open Notepad.")
            print(e)

    
    
    elif 'google search' in command:
        speak("What would you like to search for?")
        search_query = listen()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching Google for {search_query}.")
    
    elif "wikipedia" in command:  # Check for the Wikipedia query here
        speak("What do you want to search on Wikipedia?")
        search_query = listen()
        if search_query:
            result = search_wikipedia(search_query)
            print(result)
            speak(result)
    
    
    
    elif 'who made you' in command or "who created you" in command:
        speak("I have been created by Poornima.")
    
    elif'who i am' in command:
        speak("If you talk then definitely your human")
    
    elif'who are you'in command:
        speak("I am your virtual assistant created by Poornima")

    elif 'reason for you' in command:
        speak("I was created as a Minor project by M Poornima")

    
    elif 'time' in command:
        # current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_time = datetime.now().strftime("%H:%M:%S")

        speak(f"The current time is {current_time}")
        print(f"The current time is {current_time}")
        
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye! Have a nice day.")
        return True

    elif 'translate' in command:
        speak("What do you want me to translate to Tamil?")
        text_to_translate = listen()
        if text_to_translate:
            translated_text = translate_to_tamil(text_to_translate)
            if translated_text:
                speak(f"The translation is: {translated_text}")
            else:
                speak("Sorry, I couldn't translate that.")
    
    else:
        speak("Sorry, I didn't understand that.")

# Main loop to keep the assistant running
if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    
    while True:
        command = listen()
        if command:
            should_exit = handle_command(command)
            if should_exit:
                break






