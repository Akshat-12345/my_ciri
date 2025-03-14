# CIRI ( MY PERSONAL AI)

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys 
import time
import pyjokes
import pyautogui
import pymongo
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ak1 import Ui_MainWindow



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# TO WISH
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("good morning sir")
    elif hour >=12 and hour< 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("i am ciri sir, please tell me how can i help you")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("akshatpocom6pro5g@gmail.com","akshat@123")
    server.sendEmail("akshatbajpai2020@gmail.com",to,content)
    server.close()

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=cf6ed7de7a8746298184bc940aaa574e"
    
    main_page = requests.get(main_url).json()
    
    # print(main page)
    articles = main_page["articles"]
    
    # PRINT(ARTICLES)
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    for i in articles:
        head.append(i["title"])
    for j in range (len(day)):
        # PRINT(F"TODAY'S {DAY[J] NEWS IS :", HEAD[J]})
        speak(f"today's {day[j]} news is: {head[j]}")
        
# GUI 
class mainthread(QThread):
    def __init__(self) :
        super(mainthread,self).__init__()
    
    def run(self):
        self.TaskExecution()

     
 # SPEECH TO TEXT
    def takecommand(self):    
        r= sr.Recognizer()
        with sr.Microphone() as source :
             print("listening....")
             r.pause_threshold = 5
             audio = r.listen(source,timeout =3,phrase_time_limit = 8)
    
        try:
             print("recognizing...")
             query = r.recognize_google(audio, language='en-in')
             print(f"user said: {query}")
    
        except Exception as e:
             speak("Say that again please...")
             return "none"
        return query

    
    def TaskExecution(self) :
    


       wish()
       while True:
        self.querry = self.takecommand().lower()
        
        # BUILDING LOGICS FOR TASKS
        if 1:
          if "open notepad" in self.querry:
              npath ="C:\\Windows\\notepad.exe"
              os.startfile(npath)
            
          elif "open command prompt" in self.querry:
              os.system("start cmd")
          
          elif "open camera" in self.querry:
              cap = cv2.VideoCapture(0)
              while True:         
                  ret, img = cap.read()
                  cv2.imshow("webcam",img)
                  k = cv2.waitKey(50)
                  if k== 27:
                      break
              cap.release()
              cv2.destroyAllWindows()
              
          elif "play music" in self.querry:
              music_dir = "C:\\music"
              songs = os.listdir(music_dir)
              rd = random.choice(songs)
              os.startfile(os.path.join(music_dir, rd))
          
          elif "ip address" in self.querry:
              ip = get("https://api.ipify.org").text
              speak(f"your IP address is {ip}")
          
          elif "wikipedia" in self.querry:
              speak("searching wikipedia....")
              self.querry=self.querry.replace("wikipedia","")
              results = wikipedia.summary(self.querry,sentences =2)
              speak("according to wikepedia")
              speak(results)
              print(results)
                
          elif "open youtube" in self.querry:
              speak("openning youtube")
              webbrowser.open("www.youtube.com")
          
          elif "open facebook" in self.querry:
              speak("openning facebook")
              webbrowser.open("www.facebook.com")
              
          elif "open stackoverflow" in self.querry:
              speak("openning stackoverflow")
              webbrowser.open("www.stackoverflow.com")
              
          elif "open whatsapp" in self.querry:
              speak("openning whatsapp")
              webbrowser.open("https://web.whatsapp.com/")
          
          elif "open icloud" in self.querry:
              speak("openning galgotias icloud")
              webbrowser.open("https://gu.icloudems.com/corecampus/index.php")
          
          elif "open lms" in self.querry:
              speak("openning galgotias lms")
              webbrowser.open("https://lms.galgotiasuniversity.org/")
          
          elif "open hotstar" in self.querry:
              speak("openning disney plus hotsar")
              webbrowser.open("https://www.hotstar.com/in/home")
          
          elif "open youtube music" in self.querry:
              speak("openning youtube music")
              webbrowser.open("https://music.youtube.com/")
         
          elif "open chatgpt" in self.querry:
              speak("openning chat gpt")
              webbrowser.open("https://chatgpt.com/")
          
          elif "open netflix" in self.querry:
              speak("openning netflix")
              webbrowser.open("https://www.netflix.com/in/")
          
          elif "open jiocinema " in self.querry:
              webbrowser.open("https://www.jiocinema.com/")
          
          elif "open google" in self.querry:
              speak("Sir, what shuld I search on google ?")
              CM = self.takecommand().lower() 
              webbrowser.open(f"{CM}")
          
          elif "open instagram" in self.querry:
              speak("openning instagram")
              webbrowser.open("https://www.instagram.com/")
          
          elif "open twitter" in self.querry:
              speak("openning X")
              webbrowser.open("https://x.com/home?lang=en")
          
          elif "send message" in self.querry:
              speak("opening whatsapp")
              kit.sendwhatmsg("+917991780850", "hello user",datetime.datetime.now().hour,datetime.datetime.now().minute+1)
          
          elif "play songs on youtube" in self.querry:
              speak("playing songs")
              kit.playonyt("arjit singh popular songs")
              
          elif "write an email" in self.querry:
            try:
               speak("what should i say")  
               content = self.takecommand().lower()
               to = "akshatmicrosoft2024@gmail.com"
               sendEmail(to,content)
               speak("email has been sent to you sir")
            
            except Exception as e:
                print(e)
          elif "you can sleep" in self.querry:
              speak("thanks for using me sir,have a good day")
              sys.exit()
          
# TO CLOSE ANY APPLICATION 
          elif "close notepad" in self.querry:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
          
          elif "set alarm" in self.querry:
              nn = int(datetime.datetime.now().hour)
              if nn == 22:
                  music_dir = "C:\\music"
                  songs = os.listdir(music_dir)
                  os.startfile(os.path.join(music_dir,songs[0]))

# TO FIND A JOKE
          elif "tell me a joke" in self.querry:
              joke = pyjokes.get_joke()
              speak(joke)
          
          elif "shutdown the system" in self.querry:
              os.system("shutdown/s /t 5")
          
          elif "restart the system" in self.querry:
              os.system("shutdown /r /t 5") 
          
          elif "sleep the system" in self.querry:
              os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  
          
          elif "switch the window" in self.querry:
                pyautogui.keyDown("alt")  
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                
# LATEST NEWS OF INDIA               
          elif "tell me news" in self.querry:
              speak("please wait sir,fetching the latest news")
              news()
          
          elif "where am i" in self.querry or"where we are" in self.querry:
              speak("Wait sir, let me check")
              try:
                  ipAdd = requests.get("https://api.ipify.org").text
                  print(ipAdd)
                  URL = "https://get.geojs.io/v1/ip/geo/"+ipAdd+'.json'
                  geo_requests = requests.get(URL)
                  geo_data = geo_requests.json()
                  #PRINT(GEO_DATA)
                  city = geo_data["city"]
                  # STATE = GEO_DATA["STATE"]
                  county = geo_data["country"]
                  speak(f"Sir I am not sure, but i think we are in {city} city of {county} country")
              except Exception as e:
                  speak("Sorry Sir, due to network issue I am not able to track your live location")
                  pass
              
              
          speak("do you have any other work , sir") 
 
startExecution = mainthread()                  
          
class Main(QMainWindow):
     def __init__(self):
         super().__init__()    
         self.ui = Ui_MainWindow()     
         self.ui.setupUi(self) 
         self.ui.pushButton.clicked.connect(self.startTask) 
         self.ui.pushButton_2.clicked.connect(self.close)
     
     def startTask(self):
         self.ui.movie = QtGui.QMovie("gif1.gif")
         self.ui.label.setMovie(self.ui.movie)
         self.ui.movie.start()
         self.ui.movie = QtGui.QMovie("gif2.gif")
         self.ui.label_2.setMovie(self.ui.movie)
         self.ui.movie.start()
         timer = QTimer(self)
         timer.timeout.connect(self.showTime)
         timer.start(1000)
         startExecution.start()
         
     def showTime(self):
         current_time = QTime.currentTime()
         current_date = QDate.currentDate()
         label_time = current_time.toString("hh:mm:ss")
         label_date = current_date.toString(Qt.ISODate)
         self.ui.textBrowser.setText(label_date)
         self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
ciri = Main()
ciri.show()
exit(app.exec_())

     