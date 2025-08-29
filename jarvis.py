import speech_recognition as sr  #its to tell compilor i will use this 'sr' in program instead of 'speechrecognition' that is use of as keyword

import pyttsx3 #this allow python to speak every text

import webbrowser #its built in i dont have to install it in python

recognizer = sr.Recognizer() # we make keyword'recognizer' from class recognizer 

engine = pyttsx3.init() #engine will talk to you back(jarvis voice)

newsapi = "b59a3af8984d46a98da0ae65ccf67339"

import requests 

music = {
    "i love you":"https://www.youtube.com/watch?v=BSJa1UytM8w&list=RDBSJa1UytM8w&start_radio=1",
    "tere bina":"https://www.youtube.com/watch?v=_mwqXnTEHSc&list=RD_mwqXnTEHSc&start_radio=1",
    "bayan":"https://www.youtube.com/watch?v=JVtKEX90SZ0&list=RDJVtKEX90SZ0&start_radio=1",
    "saadgi":"https://www.youtube.com/watch?v=OnYoNjmNh08&list=RDOnYoNjmNh08&start_radio=1"

}


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if  "open google" in c:
        speak("openning google")
        webbrowser.open("http://google.com")
    elif "open facebook" in c:
        speak("openning facebook")
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c:
        speak("openning youtube")
        webbrowser.open("http://youtube.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = music[song]
        webbrowser.open(link)
    elif "give headlines" in c: #when say 'headline it stimulates'.
        speak("Fetching the latest news...") #it will tell that headlines is on way.
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")# Analogy: You send your assistant to the newsroom's database (NewsAPI server) to request the front page for today's U.S. headlines.🔑 Memory Trick:Think of requests.get(...) as calling a website waiter:"Can you please bring me the top headlines?"
            data = r.json()

            '''Analogy: The assistant comes back with a box full of articles, but in coded language (JSON format).  
            🔑 Memory Trick: .json() is like unboxing or translating a coded document into readable English.'''

            articles = data["articles"][:5]

            """Analogy: There are too many articles — so you tell your assistant:
            "Just give me the top 5 headlines, not the whole newspaper."
         🔑 Memory Trick:
            [:5] is like taking first 5 pages of a book, or first 5 items in a tray — only pick what's on top!"""                                   

            for article in articles:
                speak(article["title"]) # title is best practice to use with news we can change the title with other name 
        except Exception as e:
            speak("Sorry, I couldn't fetch the news.")
            print(f"News API Error: {e}")
  


    else:
        #let openAI handle the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    #Listen for the wake word 'jarvis'
    while True:
        # obtain audio from the microphone
          # recognize speech using google cloud
        print("recognizing....")
        try:
            #takes audio from microphone
            with sr.Microphone() as source:
                print("Listening!....")
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
            if(word.lower().strip() == "jarvis"):
                speak("i m hearing, RAANAA")
                with sr.Microphone() as source:
                    print("Jarvis Active!....")
                    audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"ERROR: {e}")
