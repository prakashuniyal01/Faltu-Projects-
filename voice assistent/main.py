import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
api_key = ""

def speek(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r.requests.get(f"https://newsdata.io/api/1/news?apikey=pub_50923b417e3240b4d64ecf5d5ffbfaaf0133d&q=india")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speek(article['title'])
                
    else :
        #open ai
        pass
# speech = input("please enter your speech : ")

if __name__ == "__main__":
    # speek(speech)
    speek("Initializing jarvis...........")
    while True:
        # Listen for the wake word "jarvis"
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        print("recognizing......")
        
        try:
            with sr.Microphone() as source:
                print("Listening.........")
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speek("yes")
                # Listen for command
                with sr.Microphone( ) as source :
                    print("jarvis achvite......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
            
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))