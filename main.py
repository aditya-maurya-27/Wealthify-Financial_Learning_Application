#libraries
##########################################
from yahoo_fin.stock_info import get_live_price
from tkinter import *
import tkinter as tk
import warnings
import requests_html
import emoji
from customtkinter import *
from PIL import Image,ImageTk
import yagmail
import random
import cryptographer
import edge_tts
import asyncio
import subprocess
import qrcode
import pygame
from matplotlib.figure import Figure
import speech_recognition as sr
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import re
import mysql.connector
from matplotlib.ticker import ScalarFormatter
import threading
from flask import Flask, render_template, request
import google.generativeai as genai
print("Libraries imported successfully!")
warnings.filterwarnings("ignore")
genai.configure(api_key='AIzaSyBU8RdqlMWvVAXTuBE4vFOeZ4FpsvlmWIo')
model = genai.GenerativeModel('gemini-1.5-flash')
global conversation_history
conversation_history=[]
###########################################

#Database Connectivity
###########################################
db=mysql.connector.connect(host='localhost',
                           user='root',
                           passwd='2707',
                           database='wealthify')
cur=db.cursor()
print("Database connected successfully!")
##########################################

#Price Color Transition
##########################################
def price_color_transition(new_price, old_price):
    sequence_green=["#00FF00","#0AFF0A","#15FF15","#1FFF1F","#2AFF2A",
                    "#35FF35","#3FFF3F","#4AFF4A","#55FF55","#5FFF5F",
                    "#6AFF6A","#74FF74","#7FFF7F","#8AFF8A","#94FF94",
                    "#9FFF9F","#AAFFAA","#B4FFB4","#BFFFBF","#C9FFC9",
                    "#D4FFD4","#DFFFDF","#E9FFE9","#F4FFF4","#FFFFFF"]
    sequence_red=["#FF0000","#FF0A0A","#FF1515","#FF1F1F","#FF2A2A",
                  "#FF3535","#FF3F3F","#FF4A4A","#FF5555","#FF5F5F",
                  "#FF6A6A","#FF7474","#FF7F7F","#FF8A8A","#FF9494",
                  "#FF9F9F","#FFAAAA","#FFB4B4","#FFBFBF","#FFC9C9",
                  "#FFD4D4","#FFDFDF","#FFE9E9","#FFF4F4","#FFFFFF",]
    if(float(new_price)<float(old_price)):
        for i in range(0,25):
            live_price_label.config(text=("₹{:,.2f}".format(new_price)), font=("Calibri bold", 30), foreground=sequence_red[i])
            time.sleep(0.07)
    elif(float(new_price)>float(old_price)):
        for i in range(0,25):
            live_price_label.config(text=("₹{:,.2f}".format(new_price)), font=("Calibri bold", 30), foreground=sequence_green[i])
            time.sleep(0.07)
    else:
        live_price_label.config(text=("₹{:,.2f}".format(new_price)), font=("Calibri bold", 30))
##########################################

#Fetch Live Stock Price
##########################################
def fetch_live_price(symbol, ax, canvas):
    prices=[]
    prices.append(get_live_price(symbol))
    print("Live price fetching for " + symbol + " has started!")
    while buy_sell_window.winfo_exists():
        try:
            price=get_live_price(symbol)
            prices.append(price)
            buy_button.configure(state=NORMAL)
            sell_button.configure(state=NORMAL)
            if len(prices) > 30:
                prices.pop(0)
            update_graph(ax, canvas, prices)
            price_color_transition_thread=threading.Thread(target=price_color_transition, args=(price, prices[-2]))
            price_color_transition_thread.start()
            time.sleep(1.5)
        except:
            print(f"Error in fetching live stock prices!")
    print("Live price fetching for " + symbol + " has stopped!")
##########################################

#Update Graph
##########################################
def update_graph(ax, canvas, prices):
    ax.clear()
    ax.plot(prices, label=" Live price", color='#ee8319')
    ax.legend(facecolor="#95510f", edgecolor='#3f3f3f', loc="upper left")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('#dfdfdf')
    ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
    if prices:
        ax.scatter(len(prices) - 1, prices[-1], color='#ee8319', s=50, edgecolor='white', zorder=5)
    canvas.draw()
###########################################

#Create Plot
##########################################
def create_plot():
    fig = Figure(figsize=(1, 1), dpi=115, facecolor='#3f3f3f', edgecolor='#3f3f3f')
    ax = fig.add_subplot(111, facecolor='#3f3f3f')
    fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)
    return fig, ax
##########################################

#Wealthify_AI_Animation
##########################################
def wealthify_ai_animation():
    colors=['#ffffff', '#fffbf4', '#fff8ea', '#fff4df', '#fff0d4', '#ffecca', '#ffe8bf', '#ffe5b5', '#ffe1aa', '#ffdd9f', '#ffda95',
            '#ffd68a', '#ffd280', '#ffce75', '#ffcb6a', '#ffc760', '#ffc355', '#ffbf4a', '#ffbc40', '#ffb835', '#ffb42b', '#ffb020',
            '#ffac15', '#ffa90b', '#ffa500', '#ffa500', '#ff9e00', '#ff9700', '#ff9000', '#ff8a00', '#ff8300', '#ff7c00', '#ff7500',
            '#ff6e00', '#ff6700', '#ff6000', '#ff5900', '#ff5200', '#ff4c00', '#ff4500', '#ff3e00', '#ff3700', '#ff3000', '#ff2900',
            '#ff2200', '#ff1c00', '#ff1500', '#ff0e00', '#ff0700', '#ff0000', '#ff0000', '#ff0500', '#ff0b00', '#ff1000', '#ff1500',
            '#ff1a00', '#ff2000', '#ff2500', '#ff2a00', '#ff3000', '#ff3500', '#ff3a00', '#ff4000', '#ff4500', '#ff4a00', '#ff4f00',
            '#ff5500', '#ff5a00', '#ff5f00', '#ff6500', '#ff6a00', '#ff6f00', '#ff7400', '#ff7a00', '#ff7f00', '#ff7f00', '#ff8400',
            '#ff8a00', '#ff8f00', '#ff9400', '#ff9a00', '#ff9f00', '#ffa400', '#ffaa00', '#ffaf00', '#ffb400', '#ffba00', '#ffbf00',
            '#ffc400', '#ffca00', '#ffcf00', '#ffd400', '#ffda00', '#ffdf00', '#ffe400', '#ffea00', '#ffef00', '#fff400', '#fffa00',
            '#ffff00', '#ffff00', '#f4ff00', '#eaff00', '#dfff00', '#d4ff00', '#caff00', '#bfff00', '#b5ff00', '#aaff00', '#9fff00',
            '#95ff00', '#8aff00', '#80ff00', '#75ff00', '#6aff00', '#60ff00', '#55ff00', '#4aff00', '#40ff00', '#35ff00', '#2bff00',
            '#20ff00', '#15ff00', '#0bff00', '#00ff00', '#00ff00', '#00ff0b', '#00ff15', '#00ff20', '#00ff2a', '#00ff35', '#00ff40',
            '#00ff4a', '#00ff55', '#00ff60', '#00ff6a', '#00ff75', '#00ff80', '#00ff8a', '#00ff95', '#00ff9f', '#00ffaa', '#00ffb5',
            '#00ffbf', '#00ffca', '#00ffd4', '#00ffdf', '#00ffea', '#00fff4', '#00ffff', '#00ffff', '#00f4ff', '#00eaff', '#00dfff',
            '#00d4ff', '#00caff', '#00bfff', '#00b5ff', '#00aaff', '#009fff', '#0095ff', '#008aff', '#0080ff', '#0075ff', '#006aff',
            '#0060ff', '#0055ff', '#004aff', '#0040ff', '#0035ff', '#002bff', '#0020ff', '#0015ff', '#000bff', '#0000ff', '#0000ff',
            '#0600ff', '#0c00ff', '#1100ff', '#1700ff', '#1d00ff', '#2300ff', '#2900ff', '#2e00ff', '#3400ff', '#3a00ff', '#4000ff',
            '#4600ff', '#4b00ff', '#5100ff', '#5700ff', '#5d00ff', '#6200ff', '#6800ff', '#6e00ff', '#7400ff', '#7a00ff', '#7f00ff',
            '#8500ff', '#8b00ff', '#8b00ff', '#900bff', '#9515ff', '#9a20ff', '#9e2aff', '#a335ff', '#a840ff', '#ad4aff', '#b255ff',
            '#b660ff', '#bb6aff', '#c075ff', '#c580ff', '#ca8aff', '#cf95ff', '#d39fff', '#d8aaff', '#ddb5ff', '#e2bfff', '#e7caff',
            '#ecd4ff', '#f0dfff', '#f5eaff', '#faf4ff', '#ffffff']
    wealthify_label=CTkLabel(master=wealthify_ai_text_frame, text="Wealthify", font=('Calibri bold',50))
    wealthify_label.place(x=310, y=90)
    wealthify_ai_label=CTkLabel(master=wealthify_ai_text_frame, text="AI", font=('Calibri bold',50))
    wealthify_ai_label.place(x=520, y=90)
    wealthify_ai_statement_label=CTkLabel(master=wealthify_ai_text_frame, wraplength=750, padx=10, pady=10, text="Simplify and strengthen your savings and investments with Alexa, an AI developed by Wealthify. Specializing in stock markets, investments, savings, and a wide range of financial products, Alexa is equipped with extensive knowledge derived from over a thousand books on planning, creating, managing, and sustaining wealth. Bringing together insights from the world's foremost wealth experts, Alexa provides you with the tools for smarter financial decisions, all in one place.", font=('Calibri',18))
    wealthify_ai_statement_label.place(x=60, y=190)
    i=0
    while wealthify_ai_text_frame.winfo_exists():
        if(i<225):
            wealthify_ai_label.configure(text_color=colors[i])
            i=i+1
            time.sleep(0.08)
        else:
            i=0
##########################################

#TTS engine
##########################################
async def text_to_speech(text):
    communicate=edge_tts.Communicate(text=text, voice="hi-IN-SwaraNeural", rate="+10%")
    await communicate.save("voice.mp3")
    return
##########################################

#Voice Assistant
##########################################
def voice_assistant_function():
    r = sr.Recognizer()
    mic = sr.Microphone()
    previous_hotword = None
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # Flags (iOS)
        "]+",
        flags=re.UNICODE
    )
    with mic as source:
        print("Listening for 'Alexa'...")
        while True:
            try:
                r.adjust_for_ambient_noise(source)
                hotword = r.listen(source, phrase_time_limit=1.5)
                if previous_hotword:
                    combined_hotword = sr.AudioData(
                        previous_hotword.get_raw_data() + hotword.get_raw_data(),
                        hotword.sample_rate,
                        hotword.sample_width
                    )
                else:
                    combined_hotword = hotword
                command = r.recognize_google(combined_hotword).lower()
                if "alexa" in command:
                    print("Alexa detected!")
                    previous_hotword = None
                    while True:
                        try:
                            status_label.configure(text="Alexa is listening...", fg_color="green")
                            r.adjust_for_ambient_noise(source)
                            audio=r.listen(source, phrase_time_limit=15, timeout=None)
                            status_label.configure(text="Recognizing...", fg_color="#008090")
                            text = r.recognize_google(audio)
                            if "tumhen kisne banaya hai" in text.lower():
                                print("Aditya Maurya")
                                continue
                            conversation_history.append(f"User: {text}")
                            wealthify_ai_text_frame.destroy()
                            chat_history.tag_config("User", foreground="#ee8319", lmargin1=3, lmargin2=55)
                            chat_history.tag_config("Alexa", foreground="white", lmargin1=3, lmargin2=83)
                            chat_history.configure(state="normal")
                            chat_history.insert("end", f"You: {text}\n", "User")
                            chat_history.configure(state="disabled")
                            chat_history.see("end")
                            context = "\n".join(conversation_history)
                            status_label.configure(text="Processing...", fg_color="#d50078")
                            answer = model.generate_content(context, generation_config=genai.types.GenerationConfig(temperature=2.0))
                            answer = answer.text.strip()
                            answer = emoji_pattern.sub(r'', answer)
                            chat_history.configure(state="normal")
                            chat_history.insert("end", f"Alexa: {answer}\n\n", "Alexa")
                            chat_history.configure(state="disabled")
                            chat_history.see("end")
                            conversation_history.append(f"AI: {answer}")
                            status_label.configure(text="Transcribing...", fg_color="purple")
                            asyncio.run(text_to_speech(answer))
                            status_label.configure(text="Answering...", fg_color="#00b662")
                            pygame.mixer.init()
                            pygame.mixer.music.load("voice.mp3")
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)
                            pygame.mixer.music.stop()
                            pygame.mixer.music.unload()
                            status_label.configure(text=" ", fg_color="#ee8319")
                        except sr.UnknownValueError:
                            status_label.configure(text="Couldn't catch that", fg_color="red")
                            break
                        except sr.WaitTimeoutError:
                            status_label.configure(text="Couldn't listen", fg_color="red")
                            break
                else:
                    previous_hotword = hotword
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                status_label.configure(text="Please try again", fg_color="red")
                print(e)
                continue
            except Exception as e:
                status_label.configure(text="Please try again", fg_color="red")
                print(f"Unexpected error: {e}")
                continue
##########################################

#AI responses
##########################################
def generate_response():
    message=message_entry.get()
    if message.strip()=="":
        return
    else:
        wealthify_ai_text_frame.destroy()
        message_entry.delete(0, END)
        chat_history.tag_config("User", foreground="#ee8319", lmargin1=3, lmargin2=55)
        chat_history.tag_config("Alexa", foreground="white", lmargin1=3, lmargin2=73)
        chat_history.configure(state="normal")
        chat_history.insert("end", f"You: {message}\n","User")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        conversation_history.append(f'User: {message}')
        context="\n".join(conversation_history)
        response=model.generate_content(context, generation_config=genai.types.GenerationConfig(temperature=2.0))
        ai_response = response.text.strip()
        conversation_history.append(f'AI: {ai_response}')
        chat_history.configure(state="normal")
        chat_history.insert("end",f"Alexa: {ai_response}\n\n", "Alexa")
        chat_history.configure(state="disabled")
        chat_history.see("end") 
        return
    
def generate_response_thread():
    response_thread=threading.Thread(target=generate_response)
    response_thread.start()
##########################################

#Update Wallet Balance
##########################################
def update_balance(recieved_amount):
    global owner_balance
    shades= ['#ffffff', '#f7f7f7', '#efefef', '#e7e7e7', '#dfdfdf', '#d7d7d7', '#cfcfcf', '#c7c7c7', 
    '#bfbfbf', '#b7b7b7', '#afafaf', '#a7a7a7', '#9f9f9f', '#979797', '#8f8f8f', '#878787', 
    '#7f7f7f', '#777777', '#6f6f6f', '#676767', '#5f5f5f', '#575757', '#4f4f4f', '#474747', '#3f3f3f']
    for i in range(0,25):
        current_balance_label.config(foreground=shades[i])
        time.sleep(0.04)
    owner_balance+=int(recieved_amount)
    values_for_wallet=(owner_balance, owner_email[0])
    cur.execute("update users set balance=%s where email=%s", values_for_wallet)
    db.commit()
    current_balance_label.config(text=("₹"+str(owner_balance)))
    for i in range(24,0,-1):
        current_balance_label.config(foreground=shades[i])
        time.sleep(0.04)
##########################################

#Flask Server
##########################################
def flask_server():
    app = Flask(__name__)
    @app.route('/', methods=['GET', 'POST'])
    def home():
        recipient_name = owner_name
        first_alphabet=owner_name[0]
        correct_password = owner_password
        status = None
        received_amount = None  # Variable to store the amount
        if request.method == 'POST':
            entered_password = request.form.get('password')
            amount = request.form.get('amount')  # Get the amount entered by the user
            if entered_password == correct_password:
                status = "success"
                update_balance_thread=threading.Thread(target=update_balance, args=(amount,))
                update_balance_thread.start()
            else:
                status = "failure"
                print("Incorrect password")
        return render_template('index.html', recipient_name=recipient_name, status=status, first_alphabet=first_alphabet, correct_password=correct_password, received_amount=received_amount)
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
##########################################

#Buy_Sell_Window
##########################################
def buy_sell_window_function(button_number):
    dashboardwindow.grab_release()
    global stock_list
    global buy_sell_window
    buy_sell_window=CTkToplevel(dashboardwindow)
    buy_sell_window.resizable(False, False)
    buy_sell_window.grab_set()
    buy_sell_window.lift()
    buy_sell_window.geometry("900x600")
    buy_sell_window.title(" Transact")
    background_frame_right=CTkFrame(master=buy_sell_window, width=870, height=519, corner_radius=20, fg_color="#3f3f3f")
    background_frame_right.place(x=-20, y=42)
    background_frame_left=CTkFrame(master=buy_sell_window, width=90, height=517, corner_radius=20, fg_color="#ee8319", bg_color="#3f3f3f")
    background_frame_left.place(x=-20, y=43)
    name_of_stock=stock_list[button_number][0]
    name_of_stock_label=Label(master=background_frame_right, text=name_of_stock, font=("Calibri bold",32), background="#3f3f3f", foreground="#ee8319")
    name_of_stock_label.place(x=160, y=23)
    symbol_of_stock=stock_list[button_number][2]
    symbol_of_stock_label=Label(master=background_frame_right, text=("("+symbol_of_stock+")"), font=("Calibri bold",18), background="#3f3f3f", foreground="white")
    symbol_of_stock_label.place(x=162, y=75)
    separator_frame=CTkFrame(master=background_frame_right, fg_color="#ee8319", width=690, height=3)
    separator_frame.place(x=133, y=100)
    global live_price_label
    live_price_label=Label(master=background_frame_right, text=("fetching live price..."), font=("Calibri bold",26), background="#3f3f3f", foreground="white")
    live_price_label.place(x=162, y=140)
    fig, ax = create_plot()
    canvas = FigureCanvasTkAgg(fig, master=background_frame_right)
    canvas.draw()
    canvas.get_tk_widget().place(x=165, y=195, width=860, height=350)
    global fetch_price_thread
    fetch_price_thread=threading.Thread(target=fetch_live_price, args=(symbol_of_stock, ax, canvas))
    fetch_price_thread.start()
    global buy_button
    buy_button=CTkButton(master=background_frame_right, width=100,  height=36, text="Buy", text_color_disabled="#95510f",
                                   font=("Calibri",20), corner_radius=5, fg_color="#006500",
                                     hover_color="#00cc00", state=DISABLED, command=createaccount)
    buy_button.place(x=540, y=455)
    global sell_button
    sell_button=CTkButton(master=background_frame_right, width=100, height=36, text="Sell",  text_color_disabled="#95510f",
                                   font=("Calibri",20), corner_radius=5, fg_color="#900000",
                                     hover_color="#ee0000", state=DISABLED, command=createaccount)
    sell_button.place(x=650, y=455)
    quantity_underline_frame=CTkFrame(master=background_frame_right, width=200, height=3, fg_color="#ee8319")
    quantity_underline_frame.place(x=133, y=484)
    quantity_label=Label(master=background_frame_right, text="Quantity:", font=("Calibri",19), background="#3f3f3f", foreground="white")
    quantity_label.place(x=170, y=564)
    quantity_entry=CTkEntry(master=background_frame_right, width=110, corner_radius=0, text_color="white",
                            border_width=0, fg_color="white", font=("Calibri",19), placeholder_text="(Max:1000)", placeholder_text_color="#3f3f3f")
    quantity_entry.place(x=220, y=454)
    exchange_label=Label(master=background_frame_right, text="Exchange:", font=("Calibri",19), background="#3f3f3f", foreground="white")
    exchange_label.place(x=460, y=564)
    exchange_underline_frame=CTkFrame(master=background_frame_right, width=150, height=3, fg_color="#ee8319")
    exchange_underline_frame.place(x=363, y=484)
    exchange_optionmenu=CTkOptionMenu(master=background_frame_right, width=70, button_hover_color="#ee8319", button_color="#95510f", fg_color="#95510f",
                                       dropdown_hover_color="#ee8319", dropdown_fg_color="#95510f", values=['NSE','BSE'])
    exchange_optionmenu.place(x=460, y=454)
    buy_sell_window.mainloop()
##########################################

#Dashboard frames switching
##########################################
def pack_portfolio():
    attachment_label_stocks.place(x=500)
    attachment_label_wealthifyai.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    attachment_label_portfolio.place(x=185, y=20)
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    wealthify_ai_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    portfolio_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    frame_for_portfolio=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="#303030", border_width=3,
                                 border_color="#ee8319")
    frame_for_portfolio.place(x=220, y=15)
    welcome_text="Welcome, "+owner_name+"!"
    welcome_owner_label=Label(master=frame_for_portfolio, text=welcome_text, font="Calibri 24 bold", background="#303030",
                              foreground="#ee8319")
    welcome_owner_label.place(x=24, y=8)
    values_frame=CTkFrame(master=frame_for_portfolio, width=890, height=74, fg_color="#3f3f3f", corner_radius=5)
    values_frame.place(x=16, y=46)
    separator_frame_left=CTkFrame(master=values_frame, width=3, height=55, fg_color="#95510f", corner_radius=5)
    separator_frame_left.place(x=293, y=10)
    separator_frame_right=CTkFrame(master=values_frame, width=3, height=55, fg_color="#95510f", corner_radius=5)
    separator_frame_right.place(x=589, y=10)

    current_value_label=Label(master=values_frame, text="Current Value:", font="Calibri 17", background="#3f3f3f", foreground="#ee8319")
    current_value_label.place(x=20, y=8)

    current_value=Label(master=values_frame, text="₹10000000", font="Calibri 28", background="#3f3f3f", foreground="white")
    current_value.place(x=20, y=34)
    
    invested_value_label=Label(master=values_frame, text="Invested Value:", font="Calibri 17", background="#3f3f3f", foreground="#ee8319")
    invested_value_label.place(x=385, y=8)

    invested_value=Label(master=values_frame, text="₹10000000", font="Calibri 28", background="#3f3f3f", foreground="white")
    invested_value.place(x=385, y=34)
    
    total_returns_label=Label(master=values_frame, text="Total Returns:", font="Calibri 17", background="#3f3f3f", foreground="#ee8319")
    total_returns_label.place(x=755, y=8)

    total_returns=Label(master=values_frame, text="₹10000000", font="Calibri 28", background="#3f3f3f", foreground="white")
    total_returns.place(x=755, y=34)
    holdings_label=Label(master=frame_for_portfolio, text="Your Holdings:", font="Calibri 19", background="#303030", foreground="#ee8319")
    holdings_label.place(x=26, y=157)
    holdings_frame=CTkScrollableFrame(master=frame_for_portfolio, width=869, height=314, fg_color="#3f3f3f", corner_radius=5, scrollbar_button_color="#95510f", scrollbar_button_hover_color="#ee8319")
    holdings_frame.place(x=16, y=158)
    #cur.execute("Select stock from holdings where holder=%s",values)
    #holdings=cur.fetchall()

def pack_stocks():
    global stock_list
    global stocks_scrollable_frame
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=185, y=70)
    attachment_label_wealthifyai.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    wealthify_ai_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_stocks.place(x=220, y=15)
    frame_for_stocks.lift()

def pack_wealthifyai():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_wealthifyai.place(x=185, y=120)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    wealthify_ai_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_wealthifyai.place(x=220, y=15)
    frame_for_wealthifyai.lift()

def pack_orders():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_wealthifyai.place(x=500)
    attachment_label_orders.place(x=185, y=170)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    wealthify_ai_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_orders=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="pink", border_width=3,
                                 border_color="#ee8319")
    frame_for_orders.place(x=220, y=15)

def pack_tools():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_wealthifyai.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=185, y=220)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    wealthify_ai_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_tools=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="blue", border_width=3,
                                 border_color="#ee8319")
    frame_for_tools.place(x=220, y=15)

def pack_wallet():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_wealthifyai.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=185, y=420)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    wealthify_ai_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_wallet.place(x=220, y=15)
    frame_for_wallet.lift()

def pack_contactus():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_wealthifyai.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=185, y=470)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    wealthify_ai_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    frame_for_contactus=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="purple", border_width=3,
                                 border_color="#ee8319")
    frame_for_contactus.place(x=220, y=15)
##########################################

# OTP Generation
##########################################
def generate_OTP():
    global email
    reciever=email
    global otp
    print("Generating OTP...")
    otp=random.randint(100000,999999)
    global generated_otp
    generated_otp=otp
    print("Sending OTP...")
    yag=yagmail.SMTP('wealthify.broking@gmail.com', 'wnbs fqer bktd vlad')
    subject='Login Verification'
    body=("DO NOT SHARE!\n\nYour one time password (OTP) for signing-in to your Wealthify Demat Account is '"+str(otp)+"'.\n\nIf the login attempt was not made by you, please instantly report us back on wealthify.broking@gmail.com.\n\nRegards,\nTeam Wealthify.")
    try:
        yag.send(reciever, subject, body)
        print("OTP sent successfully!")
    except:
        print("OTP delivery failed, Internet connection not found!")

def generate_OTP_thread():
    otp_thread = threading.Thread(target=generate_OTP)
    otp_thread.start()
##########################################

#Dashboard
##########################################
def dashboard(user):
    global dashboardwindow
    global owner_email
    global owner_balance
    global owner_password
    owner_email=[user]
    print("Logged-in as ",owner_email[0])
    cur.execute("select name, balance, password from users where email=%s",owner_email)
    global owner_name
    details=cur.fetchone()
    owner_name=details[0]
    owner_balance=details[1]
    owner_password=cryptographer.decrypt(details[2])
    dashboardwindow=CTkToplevel(loginwindow)
    dashboardwindow.geometry("1200x700")
    dashboardwindow.title(" Dashboard")
    dashboardwindow.resizable(False, False)
    dashboardwindow.grab_set()
    global rightframedashboard
    rightframedashboard=CTkFrame(master=dashboardwindow, corner_radius=20, border_width=0, fg_color="#3f3f3f", width=1163, height=530)
    rightframedashboard.place(x=0,y=135)
    global leftframedashboard
    leftframedashboard=CTkFrame(master=dashboardwindow, corner_radius=20, border_width=0, fg_color="#ee8319", bg_color="#3f3f3f",
                                            width=220, height=529.7)
    leftframedashboard.place(x=-20,y=135)
    global upperframedashboard
    upperframedashboard=CTkFrame(master=dashboardwindow, corner_radius=0, border_width=0, fg_color="#ee8319", width=1200, height=100)
    upperframedashboard.place(x=0,y=0)
    logophoto=ImageTk.PhotoImage(Image.open("logoimage.png"))
    logolabel=Label(master=upperframedashboard, image=logophoto, background="#ee8319")
    logolabel.place(x=30,y=11)
    headlabeldashboard=tk.Label(master=upperframedashboard, text="Wealthify", font="Calibri 45 bold",
                                background="#ee8319", foreground="white")
    headlabeldashboard.place(x=150,y=22)
    global status_label
    status_label=CTkLabel(master=upperframedashboard, width=225, height=38, text=" ", font=("Calibri",19),
                                fg_color="#ee8319", corner_radius=10)
    status_label.place(x=938, y=30)
    global portfolio_button
    portfolio_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Portfolio", hover_color="#95510f", command=pack_portfolio)
    portfolio_button.place(x=41,y=20)
    global stocks_button
    stocks_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Stocks", hover_color="#95510f", command=pack_stocks)
    stocks_button.place(x=41,y=70)
    global wealthify_ai_button
    wealthify_ai_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Wealthify AI", hover_color="#95510f", command=pack_wealthifyai)
    wealthify_ai_button.place(x=41,y=120)
    global orders_button
    orders_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Orders", hover_color="#95510f", command=pack_orders)
    orders_button.place(x=41,y=170)
    global tools_button
    tools_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Tools", hover_color="#95510f", command=pack_tools)
    tools_button.place(x=41,y=220)
    global wallet_button
    wallet_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Wallet", hover_color="#95510f", command=pack_wallet)
    wallet_button.place(x=41,y=420)
    global contact_us_button
    contact_us_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                            fg_color="#95510f", text="Contact Us", hover_color="#95510f", command=pack_contactus)
    contact_us_button.place(x=41,y=470)
    global attachment_label_contactus
    global attachment_label_wealthifyai
    global attachment_label_orders
    global attachment_label_portfolio
    global attachment_label_stocks
    global attachment_label_wallet
    global attachment_label_tools
    attachment_label_portfolio=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_portfolio.place(x=500,y=0)
    attachment_label_stocks=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_stocks.place(x=500,y=0)
    attachment_label_wealthifyai=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_wealthifyai.place(x=500,y=0)
    attachment_label_orders=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_orders.place(x=500,y=0)
    attachment_label_tools=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_tools.place(x=500,y=0)
    attachment_label_wallet=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_wallet.place(x=500,y=0)
    attachment_label_contactus=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
    attachment_label_contactus.place(x=500,y=0)
    frame_for_quote=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="#3f3f3f")
    frame_for_quote.place(x=225, y=20)
    quote='\nकहने वाले यह तो कह गए की दौलत साथ नही जाएगी,\n\nपरंतु यह कहना भूल गए कि मरते दम तक यही काम आएगी।\n\n\n\n\n\nWealth fuels endless possibilities'
    quotes_label=Label(master=frame_for_quote, text=quote, font="Calibri 25 bold", foreground="#ee8319", background="#3f3f3f")
    quotes_label.place(relx=0.15, rely=0.32)
    global frame_for_stocks
    frame_for_stocks=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="#303030", border_width=3,
                                 border_color="#ee8319")
    stocks_scrollable_frame=CTkScrollableFrame(master=frame_for_stocks, width=862, label_anchor="w",
                                               label_text="  S.n.     Stock                                                                       Symbol                                                Transact",
                                               label_fg_color="#ee8319",height=410, fg_color="#3f3f3f", corner_radius=5,
                                               scrollbar_button_color="#95510f", scrollbar_button_hover_color="#ee8319",
                                               label_font=("Calibri",20))
    stocks_scrollable_frame.place(x=20, y=20)
    cur.execute("select stock, price, symbol from stocks")
    global stock_list
    stock_list=cur.fetchall()
    for i in range(0,len(stock_list)):
        serial_number=str(i+1)+"."
        stock_frame=CTkFrame(master=stocks_scrollable_frame, width=850, height=50, fg_color="#95510f")
        serial_number_label=Label(master=stock_frame, text=serial_number, font="Calibri 18", foreground="white", background="#95510f")
        serial_number_label.place(x=20, y=12)
        stock_name_label=Label(master=stock_frame, text=(stock_list[i][0]), font="Calibri 18", foreground="white", background="#95510f")
        stock_name_label.place(x=78, y=12)
        stock_symbol_label=Label(master=stock_frame, text=(stock_list[i][2]), font="Calibri 18", foreground="white", background="#95510f")
        stock_symbol_label.place(x=557, y=12)
        buy_sell_button=CTkButton(master=stock_frame, text="Buy/Sell", font=("Calibri",16), fg_color="#ee8319", hover_color="#3f3f3f", width=100, height=30, corner_radius=5, command=lambda btn=i:buy_sell_window_function(btn))
        buy_sell_button.place(x=732, y=10)
        stock_frame.pack(pady=2)
    conversation_history.append(f"Instructions : I'm {owner_name}. You're an AI assistant named Alexa, integrated into a stock broking application called Wealthify. Your role is to guide users on financial products and help them build wealth. Respond like a natural girl—humorous, sweet, and knowledgeable. Chat history will be provided for context; 'User:' refers to me, and 'AI:' refers to you, Alexa. Focus on replying only to the most recent user message, considering the entire conversation. Avoid repeating responses from earlier in the chat. If you cannot provide specific data, politely say it's unavailable. Remember small details shared by the user to personalize future interactions. Be on point-accurate, and relevant. Do not use any kind of prefix(such as 'AI:') in your responses.")
    global frame_for_wealthifyai
    frame_for_wealthifyai=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="#303030", border_width=3,
                                 border_color="#ee8319")
    global chat_history
    chat_history=CTkTextbox(frame_for_wealthifyai, wrap="word", width=884, height=405, font=("Calibri",20), fg_color="#3f3f3f", bg_color="#303030", corner_radius=8, state="disabled")
    chat_history.place(x=20, y=20)
    global wealthify_ai_text_frame
    wealthify_ai_text_frame=CTkFrame(master=frame_for_wealthifyai, width=884, height=405, fg_color="#3f3f3f")
    wealthify_ai_text_frame.place(x=20, y=20)
    wealthify_ai_animation_thread=threading.Thread(target=wealthify_ai_animation)
    wealthify_ai_animation_thread.start()
    typing_frame=CTkFrame(master=frame_for_wealthifyai, width=884, height=50, fg_color="#582d00", corner_radius=8)
    typing_frame.place(x=20, y=430)
    global message_entry
    message_entry=CTkEntry(master=typing_frame, width=770, corner_radius=0, text_color="white", border_width=0, fg_color="#582d00", font=("Calibri",20), placeholder_text="Type your message...")
    message_entry.place(x=16, y=11)
    message_entry.bind("<Return>", lambda event: generate_response_thread())
    entry_vertical_frame=CTkFrame(master=typing_frame, width=4, height=34, fg_color="#ee8319")
    entry_vertical_frame.place(x=12, y=8)
    send_button=CTkButton(master=typing_frame, text="Send", font=("Calibri",20), width=80, hover_color="#95510f", height=38, fg_color="#ee8319", corner_radius=8, command=generate_response_thread)
    send_button.place(x=796, y=6)
    voice_assistant=threading.Thread(target=voice_assistant_function)
    voice_assistant.start()

    if __name__ == '__main__':
        server = threading.Thread(target=flask_server, daemon=True)
        server.start()

    global frame_for_wallet
    frame_for_wallet=CTkFrame(master=rightframedashboard, width=924, height=500, corner_radius=20, fg_color="#303030", border_width=3,
                                 border_color="#ee8319")
    wallet_frame=CTkFrame(master=frame_for_wallet, width=884, height=460, fg_color="#3f3f3f")
    wallet_frame.place(x=20, y=20)
    current_balance_text_label=Label(master=wallet_frame, text="Current Balance:",  font="Calibri 20", background="#3f3f3f", foreground="#ee8319")
    current_balance_text_label.place(x=20, y=10)
    global current_balance_label
    current_balance_label=Label(master=wallet_frame, text=("₹"+str(owner_balance)), font="Calibri 35 bold", background="#3f3f3f", foreground="white")
    current_balance_label.place(x=20, y=39)

    scan_and_pay_label=CTkLabel(master=wallet_frame, text="----- Scan & Pay -----\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSecured with Wealthify's expertise", font=("Calibri", 15), text_color="silver", fg_color="#3f3f3f")
    scan_and_pay_label.place(x=69, y=106)

    qr = qrcode.QRCode(box_size=9, border=1)
    qr.add_data(tunnel_url)
    qr.make(fit=True)
    qr_img=qr.make_image(fill_color="#ee8319", back_color="#3f3f3f")
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label = tk.Label(master=wallet_frame, image=qr_photo)
    qr_label.place(x=55, y=157)

    payment_notification_switch=CTkSwitch(master=wallet_frame, text="Payment sound notifications", font=("Calibri",18), progress_color="#95510f")
    payment_notification_switch.place(x=44, y=420)
    

    separator_frame_for_wallet_horizontal=CTkFrame(master=wallet_frame, fg_color="#95510f", width=310, height=3)
    separator_frame_for_wallet_horizontal.place(x=20, y=85)
    separator_frame_for_wallet_vertical=CTkFrame(master=wallet_frame, fg_color="#95510f", width=3, height=430)
    separator_frame_for_wallet_vertical.place(x=350, y=15)

    transactions_frame=CTkScrollableFrame(master=wallet_frame, width=480, height=378, corner_radius=5, scrollbar_button_color="#95510f",
                                          scrollbar_button_hover_color="#ee8319", label_text="Transactions", label_font=("Calibri",20),
                                          label_fg_color="#ee8319")
    transactions_frame.place(x=367, y=14)

    dashboardwindow.mainloop()
##########################################

#authentication
##########################################
def authenticate_OTP():
    global OTP_entry
    global OTP_frame
    global TFA_warning_label
    global generated_otp
    global email
    entered_otp=OTP_entry.get()
    if(len(entered_otp)==0):
        TFA_warning_label.configure(text="OTP field is empty, please enter the OTP!", text_color="red")
        TFA_warning_label.place_configure(relx= 0.233)
    else:
        if(entered_otp==str(generated_otp)):
            OTP_frame.destroy()
            LW_emailentry.delete(0, tk.END)
            LW_passwordentry.delete(0, tk.END)
            MW_warning_label.configure(text="Please sign-in with your credentials.", text_color="white")
            MW_warning_label.place(relx= 0.574, rely=0.745)
            dashboard(email)
        else:
            TFA_warning_label.configure(text="Wrong OTP! Please try again carefully!", text_color="red")
            TFA_warning_label.place_configure(relx= 0.254)

def authenticate_password():
    global email
    email=LW_emailentry.get()
    password=LW_passwordentry.get()
    if (len(email)==0 or len(password)==0):
        MW_warning_label.configure(text="Please fill the required fields before signing-in!", text_color="red")
        MW_warning_label.place_configure(relx=0.53)
    else:
        cur.execute('SELECT email from users')
        list_of_emails=cur.fetchall()                                              
        for i in range(0,len(list_of_emails)):
            if(email==list_of_emails[i][0]):
                cur.execute('SELECT password FROM users WHERE email=%s',list_of_emails[i])
                password_from_database=cur.fetchone()
                if(password==cryptographer.decrypt(password_from_database[0])):
                    global bottomframeright
                    global lockphoto
                    global generated_otp
                    global OTP_frame
                    generate_OTP_thread()
                    OTP_frame=CTkFrame(master=bottomframeright, fg_color="#3f3f3f", bg_color="#3f3f3f", width=570,
                                        height=360, corner_radius=20)
                    OTP_frame.place(x=400 , y=10)
                    TFA_headlabel=Label(master=OTP_frame, text="Two Factor Authentication" , background="#3f3f3f",
                                foreground="#ee8319", font="Calibri 30 bold")
                    TFA_headlabel.place(x=135, y=40)
                    TFA_label=CTkLabel(master=OTP_frame, text="Please verify that it's you by entering the six digit one time\npassword (OTP) we just sent to your registered Email\ni.e., "+email,
                                        font=("Calibri",18), text_color="white", bg_color="#3f3f3f")
                    TFA_label.place(relx= 0.128, rely=0.26)
                    otp_photo_label=Label(master=OTP_frame, image=lockphoto,  borderwidth=0)
                    otp_photo_label.place(x=220, y=226)
                    underline_otp=CTkFrame(master=OTP_frame, width=220, height=3, bg_color="#3f3f3f", fg_color="#ee8319")
                    underline_otp.place(x=170, y=215)
                    global OTP_entry
                    OTP_entry=CTkEntry(master=OTP_frame, width=180, corner_radius=0, text_color="#ee8319",
                                            border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="OTP here")
                    OTP_entry.place(x=200, y=185)
                    OTP_submit_button=CTkButton(master=OTP_frame, width=130, height=30, text="Submit", font=("Calibri",18),
                                    fg_color="#ee8319", hover_color="#95510f", corner_radius=8, command=authenticate_OTP)
                    OTP_submit_button.place(x=215, y=252)
                    global TFA_warning_label
                    TFA_warning_label=CTkLabel(master=OTP_frame, text="Please enter the one time password (OTP).",
                                        font=("Calibri",18), text_color="white", bg_color="#3f3f3f")
                    TFA_warning_label.place(relx= 0.224, rely=0.845)
                    return
                else:
                    MW_warning_label.configure(text="Wrong password! Please try again!", text_color="red")
                    MW_warning_label.place_configure(relx=0.573)
                    return
        MW_warning_label.configure(text="No Account linked with this Email was found!", text_color="red")
        MW_warning_label.place_configure(relx=0.538)                           
##########################################

#Insert details for create account
##########################################
def insert():
    name=CA_nameentry.get()
    email=CA_emailentry.get()
    password=CA_passwordentry.get()
    tick=checkbox.get()
    values=(name, email, cryptographer.encrypt(password))
    alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
               'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
               'y', 'z',' ']
    if (len(name)==0):
        warning_label.configure(text="Name can't be empty!", text_color="red")
        return
    elif (len(email)==0):
        warning_label.configure(text="Email can't be empty!",  text_color="red")
        return
    elif (len(password)==0):
        warning_label.configure(text="Password can't be empty!",  text_color="red")
        return
    else:
        for i in name:
            if(i not in alphabets):
                warning_label.configure(text="Name can't contain numbers or symbols!",  text_color="red")
                return
        cur.execute('SELECT email from users')
        list_of_emails=cur.fetchall()
        for i in range(0, len(list_of_emails)):
            if(email==list_of_emails[i][0]):
                warning_label.configure(text="Email already linked with another account!",  text_color="red")
                return
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if(tick==0):
            warning_label.configure(text="Please confirm you're above 18 years of age!",  text_color="red")
            return
        if(re.match(pattern,email) is not None):
            global submit
            warning_label.configure(text="Account created successfully! Please exit!",  text_color="green")
            cur.execute('INSERT INTO users VALUES(%s,%s,%s)',values)
            submit.configure(state=DISABLED)
            db.commit()
        else:
            warning_label.configure(text="Invalid Email detected!",  text_color="red")
            return
##########################################

#Create account window
##########################################
def createaccount():
    global createaccountwindow
    createaccountwindow=CTkToplevel()
    createaccountwindow.title(" Create an Account")
    createaccountwindow.geometry("650x650")
    lowerframe=CTkFrame(master=createaccountwindow, width=550, height=625, corner_radius=20,
                             fg_color="#ee8319", border_width=0)
    lowerframe.place(x=50, y=-20)
    middleframe=CTkFrame(master=createaccountwindow, width=549, height=580, corner_radius=20,
                              fg_color="#3f3f3f", border_width=0, bg_color="#ee8319")
    middleframe.place(x=50, y=-20)
    upperframe=CTkFrame(master=createaccountwindow, width=549, height=120, corner_radius=20,
                             fg_color="#ee8319", bg_color="#3f3f3f", border_width=0)
    upperframe.place(x=50, y=-20)
    startwealthifying=Label(master=upperframe, text="Let's start wealthifying!",foreground="white",
                             background="#ee8319", font="Calibri 30 bold")
    namephoto=ImageTk.PhotoImage(Image.open("name.png"))
    namelabel=Label(master=middleframe, image=namephoto, borderwidth=0)
    namelabel.place(x=100, y=234)
    emailphoto=ImageTk.PhotoImage(Image.open("mail.png"))
    emaillabel=Label(master=middleframe, image=emailphoto, borderwidth=0)
    emaillabel.place(x=100, y=360)
    lockphoto=ImageTk.PhotoImage(Image.open("lock.png"))
    locklabel=Label(master=middleframe, image=lockphoto, borderwidth=0)
    locklabel.place(x=102, y=482)
    global CA_nameentry
    global CA_emailentry
    global CA_passwordentry
    global checkbox
    CA_nameentry=CTkEntry(master=middleframe, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Full Name")
    CA_nameentry.place(x=108, y=190)
    CA_emailentry=CTkEntry(master=middleframe, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Permanent Email")
    CA_emailentry.place(x=108, y=290)
    CA_passwordentry=CTkEntry(master=middleframe, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Create Password", show="₹")
    CA_passwordentry.place(x=108, y=389)
    underlineframe1=CTkFrame(master=middleframe, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
    underlineframe1.place(x=69, y=220)
    underlineframe2=CTkFrame(master=middleframe, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
    underlineframe2.place(x=69, y=320)
    underlineframe3=CTkFrame(master=middleframe, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
    underlineframe3.place(x=69, y=420)
    checkbox=CTkCheckBox(master=middleframe, fg_color="#ee8319", hover_color="#95510f", corner_radius=8,
                             text="I am above the age of 18 years.", font=("Calibri",16), onvalue=1, offvalue=0)
    checkbox.place(x=155, y=460)
    global submit
    submit=CTkButton(master=middleframe, width=130, height=30, text="Submit", font=("Calibri",18),
                           fg_color="#ee8319", hover_color="#95510f", corner_radius=8, command=insert)
    submit.place(x=205, y=510)
    startwealthifying.place(x=140, y=57)
    global warning_label
    warning_label=CTkLabel(master=lowerframe, text="Please fill the required details.", font=("Calibri bold",19))
    warning_label.place(relx=0.5, rely=0.96, anchor='center')
    createaccountwindow.resizable(False, False)
    createaccountwindow.grab_set()
    createaccountwindow.mainloop()
##########################################

#Catalogue animation
##########################################
color_sequence=['#EE8319','#EE8822','#EF8D2B','#F09234','#F0973E',
                '#F19C47','#F2A150','#F2A65A','#F3AB63','#F4B06C',
                '#F4B575','#F5BA7F','#F6BF88','#F6C491','#F7C99B',
                '#F8CEA4','#F8D3AD','#F9D8B6','#FADDC0','#FBE2C9',
                '#FBE7D2','#FCECDC','#FDF1E5','#FDF6EE','#FEFBF8',]
def animation():
    while True:
        label1=Label(master=bottomframeleft, text="Mutual Funds", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label1.place(x=70, y=385)
        for i in range(0,25):
            label1.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label1.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label2=Label(master=bottomframeleft, text="Stocks", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label2.place(x=70, y=385)
        for i in range(0,25):
            label2.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label2.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label3=Label(master=bottomframeleft, text="ETFs", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label3.place(x=70, y=385)
        for i in range(0,25):
            label3.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label3.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label4=Label(master=bottomframeleft, text="Fixed Deposits", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label4.place(x=70, y=385)
        for i in range(0,25):
            label4.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label4.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label5=Label(master=bottomframeleft, text="Gold Bonds", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label5.place(x=70, y=385)
        for i in range(0,25):
            label5.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label5.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label6=Label(master=bottomframeleft, text="PPFs", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label6.place(x=70, y=385)
        label6.config(foreground=color_sequence[i])
        for i in range(0,25):
            label6.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label6.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label7=Label(master=bottomframeleft, text="NPS", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label7.place(x=70, y=385)
        for i in range(0,25):
            label7.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label7.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label8=Label(master=bottomframeleft, text="REITs", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label8.place(x=70, y=385)
        for i in range(0,25):
            label8.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label8.config(foreground=color_sequence[i])
            time.sleep(0.07)
        label9=Label(master=bottomframeleft, text="ULIPs", foreground="white",
                    background="#ee8319", font="Calibri 30 bold")
        label9.place(x=70, y=385)
        for i in range(0,25):
            label9.config(foreground=color_sequence[i])
            time.sleep(0.07)
        for i in range(24,-1,-1):
            label9.config(foreground=color_sequence[i])
            time.sleep(0.07)
##########################################

#Generate Tunnel
##########################################
tunnel=subprocess.Popen(['loophole', 'http', '5000'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
for line in iter(tunnel.stdout.readline, ''):
    match = re.search(r'https://[^\s]+', line)
    if match:
        tunnel_url=match.group(0)
        print("Tunnel Created: ", tunnel_url)
        break
tunnel.stdout.close()
##########################################

#login window
##########################################
global loginwindow
loginwindow=CTk()
loginwindow.geometry("1024x576")
loginwindow.title("Wealthify")
loginwindow.resizable(False, False)
headframe=tk.Frame(master=loginwindow, bg="#ee8319", width=1300, height=130)
headframe.place(x=0, y=0)
logophoto=ImageTk.PhotoImage(Image.open("logoimage.png"))
logolabel=Label(master=headframe, image=logophoto, background="#ee8319")
logolabel.place(x=30,y=14)
headlabel=tk.Label(master=headframe, text="Wealthify", font="Calibri 45 bold",
                    background="#ee8319", foreground="white")
headlabel.place(x=150,y=22)
global bottomframeright
bottomframeright=CTkFrame(master=loginwindow, fg_color="#3f3f3f", width=975,
                               height=385, corner_radius=20)
bottomframeright.place(x=0 , y=150)
welcomelabel=Label(master=bottomframeright, text="Welcome to Wealthify" , background="#3f3f3f",
                    foreground="#ee8319", font="Calibri 30 bold")
welcomelabel.place(x=680, y=35)
emailphoto=ImageTk.PhotoImage(Image.open("mail.png"))
emaillabel=Label(master=bottomframeright, image=emailphoto, borderwidth=0)
emaillabel.place(x=615, y=123)
LW_emailentry=CTkEntry(master=bottomframeright, width=350, corner_radius=0, text_color="#ee8319",
                         border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Email")
LW_emailentry.place(x=522, y=99)
global lockphoto
lockphoto=ImageTk.PhotoImage(Image.open("lock.png"))
passwordlabel=Label(master=bottomframeright, image=lockphoto,  borderwidth=0)
passwordlabel.place(x=616, y=208)
LW_passwordentry=CTkEntry(master=bottomframeright, width=350, corner_radius=0, text_color="#ee8319",
                            show="₹" , border_width=0, fg_color="#3f3f3f", font=("Calibri",20), placeholder_text="Password")
LW_passwordentry.place(x=522, y=168)
LW_passwordentry.bind("<Return>", lambda event: authenticate_password())
loginbutton=CTkButton(master=bottomframeright, width=130, height=30, text="Sign-in", font=("Calibri",18),
                           fg_color="#ee8319", hover_color="#95510f", command=authenticate_password, corner_radius=8)
loginbutton.place(x=620, y=235)
underlineframeupper=CTkFrame(master=bottomframeright, width=400, height=3, bg_color="#3f3f3f",
                                  fg_color="#ee8319")
underlineframeupper.place(x=485, y=130)
underlineframelower=CTkFrame(master=bottomframeright, width=400, height=3, bg_color="#3f3f3f", fg_color="#ee8319")
underlineframelower.place(x=485, y=200)
MW_warning_label=CTkLabel(master=bottomframeright, text="Please sign-in with your credentials.",
                              font=("Calibri",18), text_color="white", bg_color="#3f3f3f")
MW_warning_label.place(relx= 0.574, rely=0.745)
newtowealthifylabel=Label(master=bottomframeright, text="New to Wealthify?", font=("Calibri 18"),
                           foreground="white", background="#3f3f3f")
newtowealthifylabel.place(x=670, y=412)
createaccountbutton=CTkButton(master=bottomframeright, width=10, text="Create an Account.",
                                   font=("Calibri",19), corner_radius=5, fg_color="#3f3f3f", text_color="#ee8319",
                                     hover_color="#3f3f3f", command=createaccount)
createaccountbutton.place(x=685, y=328)
bottomframeleft=CTkFrame(master=loginwindow, fg_color="#ee8319", bg_color="#3f3f3f",
                              width=420, height=384, corner_radius=20)
bottomframeleft.place(x=-20, y=150)
slogan1=Label(master=bottomframeleft, text="Investing today,", font="Calibri 30 bold" ,
               background="#ee8319", foreground="white")
slogan1.place(x=70, y=30)
slogan2=Label(master=bottomframeleft, text="Enjoying tomorrow.", font="Calibri 30 bold" ,
               background="#ee8319", foreground="white")
slogan2.place(x=70, y=78)
print("Initializing animations...")
animation_thread=threading.Thread(target=animation)
#animation_thread.start()
print("Wealthify is now ready!")
loginwindow.overrideredirect(False)
#loginwindow.mainloop()
##########################################

dashboard("ayushmaurya7651@gmail.com")
