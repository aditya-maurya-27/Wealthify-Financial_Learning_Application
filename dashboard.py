from tkinter import *
import tkinter as tk
from customtkinter import *
from PIL import Image,ImageTk

def pack_portfolio():
    attachment_label_portfolio.place(x=185, y=20)
    attachment_label_stocks.place(x=500)
    attachment_label_mutualfunds.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    mutual_funds_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_portfolio=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="green")
    frame_for_portfolio.place(x=225, y=20)

def pack_stocks():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=185, y=70)
    attachment_label_mutualfunds.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    mutual_funds_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_stocks=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="red")
    frame_for_stocks.place(x=225, y=20)

def pack_mutualfunds():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_mutualfunds.place(x=185, y=120)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    mutual_funds_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_mutualfunds=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="blue")
    frame_for_mutualfunds.place(x=225, y=20)

def pack_orders():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_mutualfunds.place(x=500)
    attachment_label_orders.place(x=185, y=170)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    mutual_funds_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_orders=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="pink")
    frame_for_orders.place(x=225, y=20)

def pack_tools():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_mutualfunds.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=185, y=220)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    mutual_funds_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_tools=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="purple")
    frame_for_tools.place(x=225, y=20)

def pack_wallet():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_mutualfunds.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=185, y=420)
    attachment_label_contactus.place(x=500)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    mutual_funds_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    contact_us_button.configure(fg_color="#95510f", hover_color="#95510f")
    frame_for_wallet=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="orange")
    frame_for_wallet.place(x=225, y=20)

def pack_contactus():
    attachment_label_portfolio.place(x=500)
    attachment_label_stocks.place(x=500)
    attachment_label_mutualfunds.place(x=500)
    attachment_label_orders.place(x=500)
    attachment_label_tools.place(x=500)
    attachment_label_wallet.place(x=500)
    attachment_label_contactus.place(x=185, y=470)
    portfolio_button.configure(fg_color="#95510f", hover_color="#95510f")
    stocks_button.configure(fg_color="#95510f", hover_color="#95510f")
    mutual_funds_button.configure(fg_color="#95510f", hover_color="#95510f")
    orders_button.configure(fg_color="#95510f", hover_color="#95510f")
    tools_button.configure(fg_color="#95510f", hover_color="#95510f")
    wallet_button.configure(fg_color="#95510f", hover_color="#95510f")
    contact_us_button.configure(fg_color="#3f3f3f", hover_color="#3f3f3f")
    frame_for_contactus=CTkFrame(master=rightframedashboard, width=914, height=490, corner_radius=20, fg_color="yellow")
    frame_for_contactus.place(x=225, y=20)


dashboardwindow=CTkToplevel(loginwindow)
dashboardwindow.geometry("1200x700")
dashboardwindow.resizable(False, False)


rightframedashboard=CTkFrame(master=dashboardwindow, corner_radius=20, border_width=0, fg_color="#3f3f3f", width=1163, height=530)
rightframedashboard.place(x=0,y=135)
leftframedashboard=CTkFrame(master=dashboardwindow, corner_radius=20, border_width=0, fg_color="#ee8319", bg_color="#3f3f3f",
                                 width=220, height=529.7)
leftframedashboard.place(x=-20,y=135)
upperframedashboard=CTkFrame(master=dashboardwindow, corner_radius=0, border_width=0, fg_color="#ee8319", width=1200, height=100)
upperframedashboard.place(x=0,y=0)

logophoto=ImageTk.PhotoImage(Image.open("logoimage.png"))
logolabel=Label(master=upperframedashboard, image=logophoto, background="#ee8319")
logolabel.place(x=30,y=11)

headlabeldashboard=tk.Label(master=upperframedashboard, text="Wealthify", font="Calibri 45 bold",
                    background="#ee8319", foreground="white")
headlabeldashboard.place(x=150,y=22)


portfolio_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                fg_color="#95510f", text="Portfolio", hover_color="#95510f", command=pack_portfolio)
portfolio_button.place(x=41,y=20)
stocks_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                   fg_color="#95510f", text="Stocks", hover_color="#95510f", command=pack_stocks)
stocks_button.place(x=41,y=70)
mutual_funds_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                   fg_color="#95510f", text="Mutual Funds", hover_color="#95510f", command=pack_mutualfunds)
mutual_funds_button.place(x=41,y=120)
orders_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                   fg_color="#95510f", text="Orders", hover_color="#95510f", command=pack_orders)
orders_button.place(x=41,y=170)
tools_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                fg_color="#95510f", text="Tools", hover_color="#95510f", command=pack_tools)
tools_button.place(x=41,y=220)
wallet_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                fg_color="#95510f", text="Wallet", hover_color="#95510f", command=pack_wallet)
wallet_button.place(x=41,y=420)
contact_us_button=CTkButton(master=leftframedashboard, width=155, height=40, corner_radius=10, font=("Calibri",20),
                                fg_color="#95510f", text="Contact Us", hover_color="#95510f", command=pack_contactus)
contact_us_button.place(x=41,y=470)


attachment_label_portfolio=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_portfolio.place(x=500,y=0)
attachment_label_stocks=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_stocks.place(x=500,y=0)
attachment_label_mutualfunds=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_mutualfunds.place(x=500,y=0)
attachment_label_orders=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_orders.place(x=500,y=0)
attachment_label_tools=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_tools.place(x=500,y=0)
attachment_label_wallet=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_wallet.place(x=500,y=0)
attachment_label_contactus=CTkFrame(master=leftframedashboard, width=50, height=40, fg_color="#3f3f3f", bg_color="#3f3f3f")
attachment_label_contactus.place(x=500,y=0)








dashboardwindow.mainloop()

#Portfolio
#Mutual Funds
#Stocks
#Orders
#News
#Support

