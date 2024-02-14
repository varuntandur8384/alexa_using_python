import os
import sys

import speech_recognition as sr  # this library is used to recognize the speech or command
import pyttsx3                   # this library gives voice solution
import pywhatkit                 # this is the most useful library you can do anything you what...
import datetime                  # this library is used to get the current time
import spotify
import wikipedia                 # this library is used to get information from wikipedia
import pyjokes                   # This library gives the N number jokes
import webbrowser                # This library is used to open different website
import pyautogui                 # This library is used to control mouse and keyboard

import random
from requests import get


listener = sr.Recognizer()                          # to recognizer our voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')               # here we can change voice tone of the emma by changing
engine.setProperty('voice', voices[1].id)           # the index of the voices

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        talk("good morning")
    elif 12 <= hour < 17:
        talk("good afternoon")
    else:
        talk("good evening")

    talk("I am your angel. tell me What can I do for you")
    #janet angel emma charlie ethan eve


def take_command():
    try:
        with sr.Microphone() as source:                 # here we are using microphone as input source
            print("listening....")
            listener.pause_threshold = 1
            listener.energy_threshold = 300
            voice = listener.listen(source, timeout=5, phrase_time_limit=8) # here we are calling speech recognizer to listen the source
            print("understanding....")
            command = listener.recognize_google(voice,language='en-in')  # converting voice to text using the Google api, Google will
            command = command.lower()                                                           # give the text
            print("user said:" + command)
            command = command.replace('angel', '')
           
    except:  # it will ignore when exception is happened
        talk('sorry, can you please say the command again.')
        # pass
        return 'None'

    return command

def play_music():
    music_dir = 'location of the musics'
    song = os.listdir(music_dir)            # it will list all the songs present in the directory
    print(song)
    num = len(song)                         # it will calculate the total number of songs present in the file
    random_num = random.randrange(0, num)   # it will generate random number
    print(num)
    print(random_num)
    os.startfile(os.path.join(music_dir, song[random_num]))  # it will open the file and play the first song

def play_film():
    film_dir = 'D:\\films'                     # location of the file
    film = os.listdir(film_dir)                # it will list all the films present in the directory
    print(film)
    num = len(film)                            # it will calculate the total number of films present in the file
    random_num = random.randrange(0, num)      # it will generate random number
    print(num)
    print(random_num)
    os.startfile(os.path.join(film_dir, film[random_num]))  # it will open the file and play the first song

def play(command):
    song = command.replace('play', '')
    if 'youtube' in command:
        song = song.replace('music on youtube', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
        
    elif 'spotify' in command:
        song = song.replace('music on spotify', '')
        talk('playing' + song)
        print(song)
        # pywhatkit.playonyt(song)

def open_code(command):
    talk('which code do you want')
    command = take_command()
    if 'python' in command:
        talk('which python code do you want')
        command = take_command()
        if 'newton forward interpolation' in command:
            path = "E:\\python\\final_nfip.py"
            os.startfile(path)
            print("opening")

        elif 'highest and lowest' in command:
            path = "E:\\python\\finding_high_low_number_in_list.py"
            os.startfile(path)
            print("opening")

        elif 'binary search' in command:
            path = "E:\\python\\binary_search_nptel.py"
            os.startfile(path)
            print("opening")

        elif 'average grade' in command:
            path = "E:\\python\\average_grades.py"
            os.startfile(path)
            print("opening")

        elif 'merge sort' in command:
            path = "E:\\python\\merge_sort_nptel.py"
            os.startfile(path)
            print("opening")

    elif 'arduino' in command:
        talk('which arduino code do you want')
        command = take_command()
        if 'bluetooth controlled car' in command:
            path = "C:\\Users\\varun\\Desktop\\Projects\\Robo_projects\\robo_new\\robo_new.ino"
            os.startfile(path)
            print("opening")

        elif 'line follower' in command:
            path = "C:\\Users\\varun\\Desktop\\Projects\\Robo_projects\\line_follower\\line_follower.ino"
            os.startfile(path)
            print("opening")

        elif 'digital alarm clock' in command:
            path = "C:\\Users\\varun\\Desktop\\Projects\\digital_alarm_clock\\digital_alarm_clock.ino"
            os.startfile(path)
            print("opening")

def open_application(command):
    if 'open youtube' in command:
        talk('what do you want yo search on youtube')
        command = take_command()
        webbrowser.open('youtube.com')
        # webbrowser.open_new('youtube.com')

    elif 'open google' in command:
        talk('what should i search on google')
        result = take_command()
        webbrowser.open(result)
        print('opening')

    elif 'open spotify' in command:
        webbrowser.open('spotify.com')

    elif 'open email' in command:
        webbrowser.open('gmail.com')

    elif 'open word' in command:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        os.startfile(path)
        print('opening')


def run_angel():
    while True:
        command = take_command()
        if 'wake up ' in command:
            wish_me()

            while True:
                command = take_command()
                if 'go to sleep' in command:
                    talk('Ok sir, You can call me anytime')
                    break
                
                elif 'hello' in command:
                    talk('Hello sir, How are you')

                elif 'i am fine' in command or 'good' in command:
                    talk("That's great sir")

                elif 'how are you' in command or 'what about you' in command:
                    talk('perfect sir')

                elif 'thank you' in command:
                    talk('you are welcom,sir')

                elif 'date' in command:
                    talk('sorry, I have a headache')

                elif 'are you single' in command:
                    talk('I am in relationship with wifi')

                elif 'joke' in command:
                    jokes = pyjokes.get_joke()
                    print(jokes)
                    talk(jokes)

                elif 'ip address' in command:
                    ip = get('https://api.ipify.org').text
                    print(ip)
                    talk(ip)

