import time
import datetime
import wikipedia
import pywhatkit
import requests
import webbrowser
import wolframalpha
from pywikihow import search_wikihow
import speedtest
from os import startfile
from pyautogui import click
from keyboard import press,write
from googletrans import Translator
from voice_input import Listen
from voice_output import say

# getting time
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    say(f'Time is {time}')

# getting date
def get_date():
    date = datetime.date.today()
    say(f'Today is {date}')

# getting day
def get_day():
    day = datetime.datetime.now().strftime("%A")
    say(f'Today is {day}')

def speedOfInternet():
    say('Checking Sir ....')
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correct_download = int(downloading/800000)
    uploading = speed.upload()
    correct_upload = int(uploading/800000)
    say(f'The Downloading speed is {correct_download} m/s  and \nThe Uploading speed is {correct_upload} m/s')

def break_assistant():   
    say("Ok Sir , You Can Call Me At Anytime ..")
    say("Just Say Wake Up Omar!")
    exit()

# get non input error
def get_error(query):
    query = str(query)
    if 'time' in query:
        get_time()

    elif 'date' in query:
        get_date()
    
    elif 'day' in query:
        get_day()
    
    elif "break" in query:
        break_assistant()
        
    elif 'internet speed' in query:
        speedOfInternet()


# ----------------------------------------------------------
# wolframalpha 
def wolframalpha_settings(query):
    api_key = 'WY8246-P267T477J4'
    request = wolframalpha.Client(api_key)
    response = request.query(query)
    try:
        return next(response.results).text
    except:
        say('This query Is Not Defined')

def whatsapp_message(name,message): 
    click(x=683, y=757)
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
    click(x=971, y=704)
    time.sleep(1.5)
    write(message)
    press('enter')

def whatsapp_call(name):
    click(x=683, y=757)
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
    click(x=1208, y=60)

def whatsapp_video(name):
    click(x=683, y=757)
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
    click(x=1170, y=60)

def whatsapp_chat(name):
    click(x=683, y=757)
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
  
def facebook_message(name,message): 
    click(x=650, y=757)
    time.sleep(20)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)
    time.sleep(1.5)
    click(x=766, y=706)
    time.sleep(1.5)
    write(message)
    press('enter')

def facebook_call(name): 
    click(x=650, y=757)
    time.sleep(20)
    click(x=1120, y=21)
    time.sleep(1)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)
    time.sleep(1.5)
    click(x=1233, y=55)

def facebook_video(name): 
    click(x=650, y=757)
    time.sleep(20)
    click(x=1120, y=21)
    time.sleep(1)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)
    time.sleep(1.5)
    click(x=1255, y=55)

def facebook_chat(name): 
    click(x=650, y=757)
    time.sleep(20)
    click(x=1120, y=21)
    time.sleep(1)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)


# get information from wikipedia    
def get_input_error(tag,query):
    
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(name)
        say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        query = query.replace("search for","")
        query = query.replace("searching for","")
        pywhatkit.search(query)
        res = wikipedia.summary(query,5)
        say(res)
    
    elif "YouTube" in tag:
        query = str(query).replace("YouTube","").replace("open","").replace("in YouTube","")
        query = query.replace(" ","")
        youtube = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(youtube)

    elif "website" in tag:
        query = str(query).replace("open","")
        query = query.replace(" ","")
        web = "https://www."+str(query)+".com/"
        webbrowser.open(web)

    elif "playmusic" in tag:
        query = str(query).replace("play music","").replace("play","")
        query = query.replace("youtube music","")
        query = query.replace(" ","")
        pywhatkit.playonyt(query)
    
    elif "weather" in tag:
        query = str(query).replace("weather in","")
        query = query.replace("what is weather in","")
        query = query.replace("weather for","")
        api_key = "382898aca8ccf36781e1452584f5d79a"
        root_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = f"{root_url}appid={api_key}&q={query}"
        r = requests.get(url)
        data = r.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            descr = data['weather'][0]['description']
            wind = data['wind']['speed']
            say(f"Weather Information In : {query}")
            say(f"The Weather Condition is {descr}")
            say(f"The temperature is {temp}kelvin")
            say(f"The pressure is {pressure}hPa")
            say(f"The humidity is {humidity}%")
            say(f"The speed of wind is {wind}m/s")
        else:
            say("Something Went Wrong")

    elif "temperature" in tag:
        query = str(query).replace("what is the temperature","temperature in")
        query = query.replace("temperature for","temperature in")
        say(wolframalpha_settings(query))

    elif "calculate" in tag:
        query = str(query).replace("Omar","")
        query = query.replace("multiply","*")
        query = query.replace("in","*")
        query = query.replace("into","*")
        query = query.replace("power","**")
        query = query.replace("to the power","**")
        query = query.replace("plus","+")
        query = query.replace("minus","-")
        query = query.replace("divide","/")
        query = query.replace("over","/")
        query = query.replace("div","/")
        query = query.replace("2-","2 ")
        try:
            say(f'The result is : {wolframalpha_settings(query)}')
        except:
            say("I Can Not Calculate This Query")

    elif "whatsapp message" in tag:
        say('For Whom Sir ..')
        name = Listen()
        say('Ok Sir , Tell me The Message..')
        query = Listen()
        whatsapp_message(str(name),str(query))
    
    elif "whatsapp call" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a voice call Right Now For {query} ..')
        whatsapp_call(str(query))
    
    elif "whatsapp video" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a video call Right Now For {query}..')
        whatsapp_video(str(query))

    elif "whatsapp chat" in tag:
        say('chat with Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , opening whatsapp chat with {query}..')
        whatsapp_chat(str(query))
    
    elif "facebook message" in tag:
        say('For Whom Sir ..')
        name = Listen()
        say('Ok Sir , Tell me The Message..')
        query = Listen()
        facebook_message(str(name),str(query))
    
    elif "facebook call" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a voice call Right Now For {query} ..')
        facebook_call(str(query))
    
    elif "facebook video" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a video call Right Now For {query}..')
        facebook_video(str(query))

    elif "facebook chat" in tag:
        say('chat with Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , opening facebook chat with {query}..')
        facebook_chat(str(query))
    
    elif "instagram" in tag:
        click(x=716, y=747)
    
    elif "remember that" in tag:
        rmsg = str(query).replace("remember that","")
        rmsg = rmsg.replace("remind me that","")
        say(f"You Told me to remind you that {rmsg}")
        remember = open('remind.txt','w')
        remember.write(rmsg)
        remember.close()

    elif "what do you remember" in tag:
        remember_message = open('remind.txt','r')
        say(f"You Told me to remember you that {str(remember_message.read())}")

    elif "open word" in tag:
        click(x=281, y=754)
    
    elif "open excel" in tag:
        click(x=22, y=751)
        time.sleep(2)
        write('excel')
        time.sleep(1)
        click(x=138, y=197)
    
    elif "open powerpoint" in tag:
        click(x=243, y=751)
    
    elif "open access" in tag:
        click(x=22, y=751)
        time.sleep(2)
        write('access')
        time.sleep(1)
        click(x=138, y=197)
    
    elif "open chrome" in tag:
        click(x=312, y=754)
    
    elif "open vscode" in tag:
        click(x=353, y=749)
    
    elif "open command" in tag:
        click(x=94, y=752)
    
    elif "open photoshop" in tag:
        click(x=943, y=761)
    
    elif "open outlook" in tag:
        click(x=874, y=752)
    
    elif "open jupyter" in tag:
        click(x=426, y=754)
    
    elif "open spyder" in tag:
        click(x=460, y=754)
    
    elif "open zoom" in tag:
        click(x=389, y=753)
    
    elif "open py projects" in tag:
        click(x=126, y=756)
        time.sleep(1)
        click(x=69, y=586)
        time.sleep(1)
        click(x=1089, y=149)
        click(x=1089, y=149)
    
    elif "open dj projects" in tag:
        click(x=126, y=756)
        time.sleep(1)
        click(x=69, y=586)
        time.sleep(1)
        click(x=680, y=152)
        click(x=680, y=152)
    
    elif "how to" in tag:
        say("Getting Data from the internet !")
        query = str(query).replace("Omar","")
        max_result = 1
        how_to_func = search_wikihow(query, max_result)
        assert len(how_to_func) == 1
        say(how_to_func[0].summary)
   