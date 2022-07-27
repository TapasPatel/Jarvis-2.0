from importlib.resources import path
from pickle import FALSE
import pyttsx3
import speech_recognition as sr 
import pyjokes
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui 
import requests
import notification
from bs4 import BeautifulSoup
import pyjokes
import subprocess as sp
import Avenger
from wikipedia.wikipedia import random
from PIL import Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       


def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube...')
        
      
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google...')
        
      
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            speak('opening stackoverflow...')
        
      
        elif 'open amazonprime' in query:
            webbrowser.open("www.primevideo.com")
            speak('opening amazonprime...')
        
 
        elif 'play music' in query:
            music_dir = 'C:\\Users\\dipti\\Desktop\\Tapas\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        
 
        elif 'open code' in query:
            codePath = "C:\\Users\\dipti\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)
            speak('opening code...')
        
 
        elif 'email to dipti patel' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")    

        
        elif 'tell a joke' in query:
               random_joke = pyjokes.get_joke()
               print(random_joke)
               speak(random_joke)

 
        elif 'covid stats' in query:
             html_data = requests ('https://www.worldometers.info/coronavirus/')
      
             soup = BeautifulSoup(html_data, 'html.parser')
             total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
             total_cases = total_global_row.find_all('td')[2].get_text()
             new_cases = total_global_row.find_all('td')[3].get_text()
             total_recovered = total_global_row.find_all('td')[6].get_text()
             print('total cases : ', total_cases)
             print('new cases', new_cases[1:])
             print('total recovered', total_recovered)
             notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
             notification.notify(
             title="COVID-19 Statistics",
             message=notification_message,
             timeout=5
             )
             speak("here are the stats for COVID-19")             


    
 
        elif 'open notepad' in query :
           paths ="C:\\Windows\\WinSxS\\wow64_microsoft-windows-notepad_31bf3856ad364e35_10.0.22000.1_none_cfb2d573a92990de"
           os.startfile(paths['notepad'])
           speak('opening notepad...')

 
        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com") 
            speak('opening insta....')

 
        elif 'open hotstar' in query:
            webbrowser.open("www.hotstar.com") 
            speak('opening hotstar....')

 
        elif 'open Netflix' in query:
            webbrowser.open("www.netflix.com") 
            speak('opening Netflix')


        elif 'open Geeksforgeeks' in query:
            webbrowser.open("www.geeksforgeeks") 
            speak('opening Geeksforgeeks....')


        elif 'open calculator' in query:
            path = "C:\\Windows\\WinSxS\\FileMaps\\program_files_windowspowershell_modules_pester_3.4.0_examples_calculator_96fd9fd7a4e3dc4d.cdf-ms"
            os.startfile(path)
            speak('opening calculator....')


        elif 'open v' in query:
            codePath ="C:\\Users\\Public\\Desktop\\VALORANT.lnk"
            os.startfile(codePath)
            speak('opening valorant.....')


        elif 'show movies' in query:
            movies_dir = "C:\\Users\\dipti\\Desktop\\Tapas\\movies"
            movie = os.startfile(movies_dir)
            print(movie)  



        elif 'get trending movies' in query:
            webbrowser.open ("https://editorial.rottentomatoes.com/guide/popular-movies/")
            speak('Searching google....')
            speak('this is what I found')
        
        
        elif 'get latest news' in query:
            speak('Searching google...')
            query = query.replace("wikipedia", "")
            webbrowser.open("https://timesofindia.indiatimes.com/city/ahmedabad/gujarat-hooch-tragedy-death-toll-rises-to-21/articleshow/93127801.cms")
            speak('this is what i found.')

        
        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\dipti\\Desktop\\WhatsApp.lnk"
            os.startfile(codePath)
            speak('opening whatsapp...')

        
        elif 'open telegram' in query:
            codePath = "C:\\Users\\dipti\\Desktop\\Telegram.lnk"
            os.startfile(codePath)
            speak('opening telegram...')

        
        elif 'open spotify' in query:
            codePath = "C:\\Users\\dipti\\Desktop\\Spotify.lnk"
            os.startfile(codePath)
            speak('opening spotify.....')   
 

        elif 'open filmora' in query:
            codePath = "C:\\Users\\Public\\Desktop\\Wondershare Filmora 11.lnk"
            os.startfile(codePath)
            speak('opening filmora.....')   
        

        elif 'open excel' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(codePath)
            speak('opening excel.....')   

        
        elif 'open word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(codePath)
            speak('opening word.....')   

        
        elif 'open edge' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(codePath)
            speak('opening edge.....')   

        
        elif 'open onedrive' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneDrive.lnk"
            os.startfile(codePath)
            speak('opening onedrive.....')  

        
        elif 'open powerpoint' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(codePath)
            speak('opening powerpoint.....') 

        
        elif 'open mysql' in query:
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 8.0\MySQL 8.0 Command Line Client.lnk"
            os.startfile(codePath)
            speak('opening mysql.....') 
    