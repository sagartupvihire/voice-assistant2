from googletrans import Translator
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
from pytube import YouTube
# import download
import pywhatkit
# import time73
from datetime import datetime
import requests
import winsound
from playsound import playsound
import wikipediaapi
root = Tk()


root.geometry('450x350+{}+0'.format(root.winfo_screenwidth() - 500))
command_label = Label(root, text="Command:")
# command_label.place(x=500, y=500)

from wikipediaapi import Wikipedia


import wikipediaapi

def wikipedia_search(search_term):
    command_label.config(text=search_term)
    wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    page = wiki.page(search_term)
    if page.exists():
        article_summary = page.summary
        # Create a new Toplevel window
        new_window = Toplevel(root)
        # Set the window size and make it resizable
        new_window.geometry("800x600")
        new_window.minsize(500,500)
        new_window.resizable(True, True)
        # Create a scrollbar widget
        scrollbar = Scrollbar(new_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        # Create a label widget to display the article summary
        article_label = Label(new_window, text=article_summary, justify=LEFT, width=500, height=500,wraplength=500)
        article_label.pack()
        # Configure the scrollbar
        article_label.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=article_label.yview)
        new_window.mainloop()
    else:
        messagebox.showerror("Error", "Article not found")




# def wikipedia_search(search_term):
#     wiki = Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
#     page = wiki.page(search_term)
#     if page.exists():
#         article_summary = page.summary[0:200] + "..."
#         new_window = Tk()
#         new_window.geometry('450x350')
#         article_label = Label(new_window, text=article_summary)
#         article_label.pack()
#         new_window.mainloop()
#     else:
#         messagebox.showerror("Error", "Article not found")



import smtplib

def send_email(to, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sagartup20@gmail.com", "sender_email_password")
    msg = f"Subject: {subject}\n\n{message}"
    server.sendmail("sender_email@gmail.com", to, msg)
    server.quit()

from googletransx import Translator

def translate(text, dest):
    translator = Translator()
    translated = translator.translate(text, dest)
    return translated

# Example usage
# text = "Hello World"
# dest = "fr" # French
# translated_text = translate(text, dest)
# print(translated_text) # Bonjour le monde


# def translate(text, dest):
#     translator = Translator()
#     translated = translator.translate(text, dest)
#     return translated.text

# Example usage
# text = "Hello World"
# dest = "fr" # French
# translated_text = translate(text, dest)
# print(translated_text) # Bonjour le monde

# def wikipedia_search(search_term):
#     wiki = Wikipedia(language='en')
#     page = wiki.page(search_term)
#     if page.exists():
#         article_summary = page.summary[0:200] + "..."
#         new_window = Tk()
#         new_window.geometry('450x350')
#         article_label = Label(new_window, text=article_summary)
#         article_label.pack()
#         new_window.mainloop()
#     else:
#         return "Article not found."


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    # Create a Tkinter label to display the download percentage
    download_label = Label(root, text="Downloading...")
    download_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.update()

    # Download the video in chunks and update the download label with the percentage
    response = requests.get(youtubeObject.url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    wrote = 0 
    with open(youtubeObject.default_filename, 'wb') as f:
        for data in response.iter_content(block_size):
            wrote = wrote  + len(data)
            f.write(data)
            download_label.config(text=f"{int((wrote/total_size)*100)}%")
            root.update()
    download_label.config(text="Download Complete")
    root.update()
    command_label.destroy()
    command_label = Label(root, text="YouTube video completed")
    command_label.place(relx=0.5, rely=0.9, anchor=S)

    # destroy download window after completing download
    download_label.destroy()



def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', value=125)
    engine.say(x)
    engine.runAndWait()

def change_listenBtn():
    listen_button.config(text="Listening...",padx=1, pady=1)
    listen_button.place(relx=0.5, rely=0.8, anchor=S)



def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        # speechtx('hello  i am EDITH')
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        # time.sleep(5)74
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            # print(data)
            return data
        except:  #sr.UnknownValueError()
            print("Not Understanding")
            return ''
# link = Entry(root)


from datetime import datetime, time

def set_alarm(alarm_time):
    alarm_time = datetime.strptime(alarm_time, "%H:%M").time()
    while True:
        current_time = datetime.now().time()
        if current_time == alarm_time:
            PlaySound('C:/Users/sagar/Documents/Assistant.mp3')
            break


def listen():

    command_label.config(text="Listening: ")
    listen_button.config(text = "Listening... ")
    root.update()
    winsound.Beep(2500, 500)
    data = sptext().lower()
    command_label.config(text="Command: " + data)
    listen_button.config(text = "Listen")

    print("command -> " +data)
    if "download youtube video" in data.lower():
        # link = input("link please..")
        # link.pack()
        # b = Button(text='sumbit' ,command= fun)
        # b.pack()
        input_value = simpledialog.askstring("Input", "Please enter youtube link:",
                                        parent=root)
        Download(input_value)
    if 'whatsapp' in data.lower():
        # engine = pyttsx3.init()
        # engine.say("Please Enter a number")
        # print("Enter a number")
        # number = input("Enter number ->")
        # time = datetime.now()
        input_value = simpledialog.askstring("Input", "Please enter your Number:",
                                        parent=root)
        time = datetime.now()
        pywhatkit.sendwhatmsg('+91' + input_value, "hello this side sagar", time.hour, time.minute+1)

    # if "send mail" in data.lower():
    #     to = simpledialog.askstring("Enter recipient email", "Email:")
    #     subject = simpledialog.askstring("Enter email subject", "Subject:")
    #     message = simpledialog.askstring("Enter email message", "Message:")
    #     send_email(to, subject, message)
    #     command_label.config(text="Command: Email sent to " + to)
    elif "search on wikipedia" == data.lower():
        speechtx("what do want to search")
        data2 = sptext()
        if data2 != ' ':
            info = wikipedia_search(data2)
            speechtx(info)


        
    elif "set alarm" in data.lower():
        try:
            alarm_time = simpledialog.askstring("Enter alarm time", "HH:MM")
            alarm_time = datetime.strptime(alarm_time, "%H:%M").time()
            current_time = datetime.now().time()
            if alarm_time < current_time:
                raise ValueError("Alarm time has already passed")
            set_alarm(alarm_time)
            command_label.config(text="Command: Alarm set for " + str(alarm_time))
        except ValueError as e:
            command_label.config(text="Command: " + str(e))
        except:
            command_label.config(text="Command: Incorrect time format")

    elif "translate" in data.lower():
        text = simpledialog.askstring("Enter text to translate", "Text:")
        dest = simpledialog.askstring("Enter destination language code (ex: fr for French, es for Spanish)", "Language Code:")
        translated_text = translate(text, dest)
        command_label.config(text="Command: " + translated_text)
        speechtx(translated_text)


    elif "tell a joke" in data.lower():
        joke = pyjokes.get_joke()
        command_label.config(text="" + joke)
        speechtx(joke)
    
    elif "open website" in data.lower():
        website = data.split(" ")[-1]
        webbrowser.open(website)
    # //djgjyj
    
    elif "time" in data.lower():
        current_time = datetime.now().strftime("%H:%M:%S")
        command_label.config(text="Command: " + current_time)
        speechtx(current_time)
    
    
    elif "schedule wake up" in data.lower():
        wake_up_time = data.split("at ")[-1]
        wake_up_time = datetime.strptime(wake_up_time, "%H:%M").time()
        current_time = datetime.now().time()
        time_diff = datetime.combine(datetime.today(), wake_up_time) - datetime.combine(datetime.today(), current_time)
        seconds = time_diff.total_seconds()
        pywhatkit.sendwhatmsg("+917385230278", "Wake up call", int(wake_up_time.hour), int(wake_up_time.minute), int(seconds/60), True)
        command_label.config(text="Command: Wake up call scheduled for " + str(wake_up_time))
    
    # elif "send mail" in data.lower():
    #     to = simpledialog.askstring("Enter recipient email", "Email:")
    #     subject = simpledialog.askstring("Enter email subject", "Subject:")
    #     message = simpledialog.askstring("Enter email message", "Message:")
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login("sagartup20@gmail.com", "sagar321@")
    #     msg = f"Subject: {subject}\n\n{message}"
    #     server.sendmail("sagartup20@gmail.com", to, msg)
    #     server.quit()
    #     command_label.config(text="Command: Email sent to " + to)
    else:
        command_label.config(text="Command not recognized")
    
    

root.title("Voice Assistant")

listen_button = Button(root, text="Listen", command=listen,width=7, height=2,padx=1, pady=1)


command_label = Label(root, text="Command:")
command_label.place(relx=0.5, rely=0.9, anchor=S)
listen_button.place(relx=0.5, rely=0.8, anchor=S)


playsound('C:/Users/sagar/Documents/Assistant.mp3')
root.mainloop()

