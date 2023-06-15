import telebot
import time
import random
import pyjokes
from gtts import gTTS
from password_generator import PasswordGenerator
import pyqrcode
import io
from datetime import timedelta,datetime
import requests
from telebot import types
import os
import png
from tabulate import tabulate
from API_of_adhi import API_key_Famalo,coporate_bs_api_key,API_weather_key #API keys

#bot api
token = API_key_Famalo()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):#message default parameter
    bot.reply_to(message,"Hi!\nI'm Famalo \nYour all in one buddy \nYou can choose one of the commands below ")
    bot.send_message(message.chat.id,"Ask me a joke😜- /joke") #uses pyijokes libary
    bot.send_message(message.chat.id,"Roll a dice🎲 - /dice") # uses random module
    bot.send_message(message.chat.id,"Text to audio converter🎵 - /textaudio") # use GTTS libary
    bot.send_message(message.chat.id,"PasswordGenerator 🔐 - /password") #uses password_generator libary
    bot.send_message(message.chat.id,"QR Code Generator - /qrcodegenerator") #uses pyqr code libary
    bot.send_message(message.chat.id,"Playbackspeed Calculator 📼 - /playbackspeedcalculator") #feature implemented from scratch
    bot.send_message(message.chat.id,"Coporate BS 🐂💩 - /coporatebs") #sends http request to Coporate bs api
    bot.send_message(message.chat.id,"Superhero Deatils 🦸🦹 -/super") #sends http request to super hero deatils api
    bot.send_message(message.chat.id,"Random Meme Generator 😂 -/meme")#sends http request to meme generator api
    bot.send_message(message.chat.id,"Random Activity Generator 😴🥱😃 -/activity") #sends http request to activity generator api with buttons implemented from scratch
    bot.send_message(message.chat.id,"External mark needed for specific grade🧑‍🎓 -/gradecalculator") #feature implemented from scratch(tabulate and html for output)
    bot.send_message(message.chat.id,"Weather deatils of your current location⛅ -/weather") # imeplemented using buttons from scratch and openweather api for data
    bot.send_message(message.chat.id,"Contact📱-/contact") 

@bot.message_handler(commands=['joke'])
def joke(message):
    bot.reply_to(message,"So you want a joke")
    #send GIF
    bot.send_sticker(message.chat.id,"https://media.tenor.com/7R4_EnS5IPIAAAAM/younge-sheldon-i-dont-have-time-for-jokes.gif")
    time.sleep(2) #for joke purpose
    bot.send_sticker(message.chat.id,"https://media.tenor.com/07qImC4D1ToAAAAC/i-was-just-kidding-kidding.gif")
    bot.send_message(message.chat.id,"Here is your joke")
    #Takes a joke randomly from pyjokes libary
    jokes_text=pyjokes.get_joke("en","all")
    bot.send_message(message.chat.id,jokes_text) #send joke

@bot.message_handler(commands=['dice'])
def dice(message):
    bot.reply_to(message,"So you don't have a dice with you")
    bot.send_sticker(message.chat.id,"https://media.tenor.com/ND2XiIDIX3IAAAAC/trust-me-i-got-you.gif")
    bot.send_message(message.chat.id,"In .....1....2..")
    send_sticker = bot.send_sticker(message.chat.id,"https://media.tenor.com/i_L5KauoCcoAAAAi/dice.gif")
    time.sleep(3) # for building up tension while dice is rolling
    bot.delete_message(message.chat.id,send_sticker.message_id) # stopping GIF for unwanted confusion
    number=random.randint(1,6) # random number from 1-6
    Dice_number=(f"The number is {number}")
    bot.send_message(message.chat.id,Dice_number)

@bot.message_handler(commands=['textaudio'])
def textaudio(message):
    bot.reply_to(message,"This will convert your text to audio")
    msg = bot.send_message(message.chat.id,"Enter the text")
    bot.register_next_step_handler(msg,text_to_audio_processing)
    
def text_to_audio_processing(message): #processing input of user
    text=message.text
    audio=gTTS(text=text,lang="en",slow=False) # converting it to audio
    audio.save("audio.mp3") # saving it locally
    with open("audio.mp3", "rb") as audio_file:
    # Send the audio file
        bot.send_audio(message.chat.id, audio_file)
    os.remove("audio.mp3") #delete after sending

    


@bot.message_handler(commands=['password'])
def password_generator1(message):
    bot.reply_to(message,"So you decided to bo more secure than a normal user who puts their pet's name as password")
    bot.send_sticker(message.chat.id,"https://media.tenor.com/9Ez46wr-voMAAAAC/lock.gif")
    bot.send_message(message.chat.id,"You can copy the below password and use")
    pwo = PasswordGenerator() #calling libary
    pwo1=pwo.generate() # randomly generating password
    bot.send_message(message.chat.id,pwo1)

@bot.message_handler(commands=['qrcodegenerator'])
def qrcodegenerator(message):
    bot.reply_to(message,"Say goodbye to typing long links or text. Say hello to the easy way. Just scan and let the magic unfold")
    message = bot.send_message(message.chat.id,"Type your link or text")
    bot.register_next_step_handler(message,Processing_qrcodegenerator) 


def Processing_qrcodegenerator(message): # handling user input
    text_link = message.text
    QRCode = pyqrcode.create(text_link) #creating qr code
    qr_code_image = io.BytesIO() # to avoid saving of file locally before sending it 
    QRCode.png(qr_code_image, scale=10) # scale is size
    qr_code_image.seek(0) 
    bot.send_photo(message.chat.id, qr_code_image)

@bot.message_handler(commands=['playbackspeedcalculator'])
def playbackspeedcalculator(message):
    bot.send_message(message.chat.id,"So you wanna know is it worth to watch your lecture in fast mode ")
    message = bot.send_message(message.chat.id,"Type the length of your video in this format (00:00:00)\nlimit (23:59:59)")
    bot.register_next_step_handler(message,Validating_input)

def Validating_input(message): # error management
    global time1 # for using it in all functions
    time1 = message.text
    if len(time1) == 8:
        conditions = (time1[0] in '012',time1[1] in '0123456789', # conditions for true input
                        time1[2] == ':',time1[3] in '012345',
                        time1[4] in '0123456789',time1[5] == ':',
                        time1[6] in '012345',time1[7] in '0123456789')
        if all(conditions):
            bot.send_message(message.chat.id,"OK")
            input_playback_speed(message)
        else:
            bot.send_message(message.chat.id,"Wrong input format, Try again")
            playbackspeedcalculator(message)
    else:
        bot.send_message(message.chat.id,"Wrong input format, Try again")
        playbackspeedcalculator(message)

def input_playback_speed(message):
    message = bot.send_message(message.chat.id,"Type Your playbackspeed in this format(1.50)")
    bot.register_next_step_handler(message,validating_input2)

def validating_input2(message): #error management
    speed = message.text
    if len(speed) == 4: 
        conditions = (len(speed) == 4, speed[1] == '.', speed[0] in '0123456789', # conditions for true
                        speed[2] in '0123456789', speed[3] in '0123456789')
        if all(conditions):
            bot.send_message(message.chat.id,"OK")
            calculating_sending_output(speed,message)

        else:
            bot.send_message(message.chat.id,"Wrong input format, Try again")
            input_playback_speed(message)
    else:
        bot.send_message(message.chat.id,"Wrong input format, Try again")
        input_playback_speed(message)

        
def calculating_sending_output(speed,message): # final calculation and output
    # converting to seconds
    original_total_seconds = (int(time1[0]+time1[1]) * 3600)+ (int(time1[3]+time1[4]) * 60) + (int(time1[6]+time1[7]))
    calculated_result_seconds = float(original_total_seconds)/float(speed) # result
    rounded_calculated_result_seconds = round(calculated_result_seconds, 0) # removing decimal part
    result_time = timedelta(seconds=rounded_calculated_result_seconds) # changing format
    bot.send_message(message.chat.id,f"Calculated Time = {result_time}")  # send
    datetime1 = datetime.strptime(time1,"%H:%M:%S")
    datetime2 = datetime.strptime(str(result_time),"%H:%M:%S")
    saved_time = datetime1 - datetime2 # subracting to find saved time
    bot.send_message(message.chat.id,f"Time you can save at {speed} = {saved_time}") #send saved time
    
@bot.message_handler(commands=['coporatebs'])
def coporatebs(message):
    url = "https://sameer-kumar-corporate-bs-generator-v1.p.rapidapi.com/" #url of api
    
    #get response from api
    response = requests.get(url, headers= coporate_bs_api_key()) #api key and host
    #converting it to dictionary from json
    phrase = response.json()
    bot.send_message(message.chat.id,"So you wanna here some Coporate 🐂💩\nWhich makes no sense\nBut sounds complex🤔😵‍💫")
    bot.send_message(message.chat.id,phrase['phrase']) # sending phrase
    bot.send_sticker(message.chat.id,"https://media.tenor.com/bkbcsCcDMJIAAAAC/try-to-figure-it-out-emma.gif")

@bot.message_handler(commands=['super'])
def super(message):
    bot.send_message(message.chat.id,"So you wanna know the deatils of your favourite Superhero/Villian")
    bot.send_message(message.chat.id,"Go to this website and send me the ID of your Superhero/Villian")
    #asking user to send id
    bot.send_message(message.chat.id,"https://www.superheroapi.com/ids.html")
    message = bot.send_message(message.chat.id,"You can use 'Find in page' feature of your browser")
    bot.send_message(message.chat.id,"For Random send a number between (1-731)")
    bot.register_next_step_handler(message,processing_sending_deatils) # taking input

def processing_sending_deatils(message):
    id = message.text
    url = f'https://superheroapi.com/api/248489081095040/{id}'
    response = requests.get(url)
    deatils = response.json()
    #if id not found try again
    try:
        bot.send_message(message.chat.id,deatils['name'])
    except KeyError:
        bot.send_message(message.chat.id,'ID not found, Try again')
        super(message)
    #send photo of super hero
    image_url = str(deatils['image']['url'])
    bot.send_photo(message.chat.id,image_url)
    data = deatils
    #avoid repeated data
    del data['name']
    del data['response']
    del data['image']
    #organising nested dictionary data in a string for readability
    def get_nested_dictionary_string(data, indent=0):
        result = ""
        for key, value in data.items():
            if isinstance(value, dict):
                result += '\t' * indent + f'{key}:\n'
                result += get_nested_dictionary_string(value, indent + 1)
                result += '\n'
            else:
                result += '\t' * indent + f'{key}: {value}\n'
                result += '\n'
        return result
    #sending string
    bot.send_message(message.chat.id,get_nested_dictionary_string(data))

@bot.message_handler(commands=['meme'])
def meme(message):
    bot.reply_to(message,"Here is a random meme for you")
    #meme api response
    response = requests.get('https://meme-api.com/gimme')
    meme = response.json()
    meme_url = meme['url']
    if meme_url[-1:-4:-1] =='fig': #gif written backwards
        # if it is a gif
        bot.send_sticker(message.chat.id,meme_url)
    else:
        # else photo
        bot.send_photo(message.chat.id,meme_url)

@bot.message_handler(commands=['activity'])
def activity(message):
    #inline keyboard buttons
    keyboard = types.InlineKeyboardMarkup()
    option1 = types.InlineKeyboardButton("Education", callback_data='education')
    option2 = types.InlineKeyboardButton("Recreational", callback_data='recreational')
    option3 = types.InlineKeyboardButton("Social",callback_data='social')
    option4 = types.InlineKeyboardButton("DIY",callback_data = 'diy')
    option5 = types.InlineKeyboardButton("Charity",callback_data='charity')
    option6 = types.InlineKeyboardButton("Cooking",callback_data='cooking')
    option7 = types.InlineKeyboardButton("Relaxation",callback_data='relaxation')
    option8 = types.InlineKeyboardButton("Music",callback_data='music')
    option9 = types.InlineKeyboardButton("Busywork",callback_data='busywork')
    option10 = types.InlineKeyboardButton("Any",callback_data='any')
    #defining keyboard
    keyboard.add(option1, option2,option3,option4,option5,option6,option7,option8,option9,option10)
    bot.send_message(message.chat.id,"So your bored and don't know what to do\nI will help you")
    bot.send_message(message.chat.id, 'Choose a Catergory of Activity:', reply_markup=keyboard) #calling buttons below this message

@bot.callback_query_handler(func=lambda call: True)
def callback_query_send_response(call):
    #responses for each button
    if call.data == 'any':
        response = requests.get('http://www.boredapi.com/api/activity/')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    #generally requesting a different response for different type
    elif call.data == 'education':
        type = 'education'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'recreational':
        type = 'recreational'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'social':
        type = 'social'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'diy':
        type = 'diy'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'charity':
        type = 'charity'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'cooking':
        type = 'cooking'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'relaxation':
        type = 'relaxation'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'music':
        type = 'music'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])
    elif call.data == 'busywork':
        type = 'busywork'
        response = requests.get(f'http://www.boredapi.com/api/activity?type={type}')
        data = response.json()
        bot.send_message(call.message.chat.id, data['activity'])

@bot.message_handler(commands=['gradecalculator'])
def gradecalculator(message):
    bot.send_message(message.chat.id,"This calculator will tell the external marks required for each grade according to your internal mark")
    bot.send_photo(message.chat.id,"https://imgtr.ee/images/2023/06/05/bAsnI.png")
    bot.send_message(message.chat.id,"This will be used as reference for calculation")
    bot.send_message(message.chat.id,"Enter your total internal mark(15 or 20)")
    bot.register_next_step_handler(message,total_internal_mark_validation)

def total_internal_mark_validation(message):
    total_internal_mark = message.text
    total_internal_mark = int(total_internal_mark)
    if total_internal_mark in (20,15):
        bot.send_message(message.chat.id,"OK")
        bot.send_message(message.chat.id,f"Enter your internal mark (out of {total_internal_mark})")
        bot.register_next_step_handler(message,internal_mark_validation,total_internal_mark)
    else:
        bot.send_message(message.chat.id,"Wrong input! Try again")
        gradecalculator(message) 

def internal_mark_validation(message,total_internal_mark):
    internal_mark = message.text
    internal_mark = int(internal_mark)
    if internal_mark <= total_internal_mark and internal_mark >= 0 :
        bot.send_message(message.chat.id,"OK")
        list_with_internal_total_internal = [internal_mark,total_internal_mark]
        send_output(message,list_with_internal_total_internal)
    else:
        bot.send_message(message.chat.id,"Wrong input! Try again")
        gradecalculator(message)


def send_output(message,list_with_internal_total_internal):
    internal_mark = list_with_internal_total_internal[0]
    total_internal_mark = list_with_internal_total_internal[1]
    if total_internal_mark == 20:
        total_mark = 100
        total_external_mark = 80
    elif total_internal_mark == 15:
        total_mark = 75
        total_external_mark = 60
    O_grade = (total_mark  * 95/100 ) - internal_mark 
    A1_grade = (total_mark  * 85/100 ) - internal_mark 
    A2_grade = (total_mark  * 75/100 ) - internal_mark 
    B1_grade = (total_mark  * 65/100 ) - internal_mark 
    B2_grade = (total_mark  * 55/100 ) - internal_mark 
    C_grade = (total_mark  * 45/100 ) - internal_mark 
    P_grade = (total_mark  * 35/100) - internal_mark
    F_grade = f"Below {P_grade}" 
    list_with_External_Marks = [O_grade,A1_grade,A2_grade,B1_grade,B2_grade,C_grade,P_grade,F_grade]
    for i in range(len(list_with_External_Marks)-1):
        if list_with_External_Marks[i] > total_external_mark:
            list_with_External_Marks[i] = "Not possible"
        else:
            list_with_External_Marks[i] = "Above " + str(list_with_External_Marks[i])
    data = [["O",list_with_External_Marks[0]],
            ["A+",list_with_External_Marks[1]],
            ["A",list_with_External_Marks[2]],
            ["B+",list_with_External_Marks[3]],
            ["B",list_with_External_Marks[4]],
            ["C",list_with_External_Marks[5]],
            ["P",list_with_External_Marks[6]],
            ["F",list_with_External_Marks[7]]]
    #converts list to a table with borders 
    table_string = tabulate(data, headers=["Grade","External marks Needed"], tablefmt="grid",colalign=("left", "left"))
    table_html = f"<pre>{table_string}</pre>" #used html for making borders uniform (according to data)
    bot.send_message(message.chat.id, text=table_html, parse_mode="HTML")
@bot.message_handler(commands=['weather'])
def weather(message):
    #defining Send Location button
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_location = types.KeyboardButton(text="Send Location", request_location=True)
    keyboard_markup.add(button_location)
    
    # Send the message with the request for location
    bot.send_message(message.chat.id, "Please send your location.", reply_markup=keyboard_markup)
    bot.register_next_step_handler(message,handle_location)

def handle_location(message):
    #taking input from user and storing data in specific variables
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    remove_keyboard_command = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Location identified", reply_markup=remove_keyboard_command)
    send_output_weather(message,latitude,longitude)

def send_output_weather(message,latitude,longitude):
    API_weather = API_weather_key()
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_weather}&units=metric")
    data = response.json()
    print(data)
    #assigning each variable to a data from response
    name = data['name']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Sending the extracted data to user
    bot.send_message(message.chat.id, f"Name: {name}")
    bot.send_message(message.chat.id, f"Description: {description}")
    bot.send_message(message.chat.id, f"Temperature: {temp}°C")
    bot.send_message(message.chat.id, f"Feels like: {feels_like}°C")
    bot.send_message(message.chat.id, f"Minimum Temperature: {temp_min}°C")
    bot.send_message(message.chat.id, f"Maximum Temperature: {temp_max}°C")
    bot.send_message(message.chat.id, f"Pressure: {pressure} hPa")
    bot.send_message(message.chat.id, f"Humidity: {humidity}%")
    bot.send_message(message.chat.id, f"Wind Speed: {wind_speed} m/s")
    #forecast data can be added in the future

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.reply_to(message,"So you wanna contact the developer")
    bot.send_message(message.chat.id,"Here you go")
    bot.send_message(message.chat.id,"@ADHIVP") #telegram user id 

bot.infinity_polling()