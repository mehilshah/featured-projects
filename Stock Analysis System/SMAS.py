import numpy as np
import tkinter as tk
import sqlite3
from tkinter import *
import tkinter.messagebox
import quandl
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import pandas as pd
quandl.ApiConfig.api_key = 'iTy4h6zHbkLX5_4o8_GA'

win=Tk()
win.title("Stock Management and Analysis System")
win.geometry("500x500")

def RSI(data1):
    close = data1['Close']
    # Get the difference in price from previous step
    delta = close.diff()
    # Get rid of the first row, which is NaN since it did not have a previous 
    # row to calculate the differences
    delta = delta[1:] 

    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    # Calculate the EWMA
    roll_up1 = pd.stats.moments.ewma(up, 14)
    roll_down1 = pd.stats.moments.ewma(down.abs(), 14)

    # Calculate the RSI based on EWMA
    RS1 = roll_up1 / roll_down1
    RSI1 = 100.0 - (100.0 / (1.0 + RS1))

    # Calculate the SMA
    roll_up2 = pd.rolling_mean(up, 14)
    roll_down2 = pd.rolling_mean(down.abs(), 14)

    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))

    # Compare graphically
    plt.figure()
    RSI1.plot()
    RSI2.plot()
    plt.title("Relative Strength Index")
    plt.legend(['RSI via EWMA', 'RSI via SMA'])
    plt.show()

def RSI_CSA(data2,data3):
    close2 = data2['Close']
    close3 = data3['Close']
    # Get the difference in price from previous step
    delta2 = close2.diff()
    delta3 = close3.diff()
    # Get rid of the first row, which is NaN since it did not have a previous 
    # row to calculate the differences
    delta2 = delta2[1:]
    delta3 = delta3[1:]

    # Make the positive gains (up) and negative gains (down) Series
    up2, down2 = delta2.copy(), delta2.copy()
    up2[up2 < 0] = 0
    down2[down2 > 0] = 0
    up3, down3 = delta3.copy(), delta3.copy()
    up3[up3 < 0] = 0
    down3[down3 > 0] = 0
    
    # Calculate the EWMA
    roll_up2 = pd.stats.moments.ewma(up2, 14)
    roll_down2 = pd.stats.moments.ewma(down2.abs(), 14)
    roll_up3 = pd.stats.moments.ewma(up3, 14)
    roll_down3 = pd.stats.moments.ewma(down3.abs(), 14)

    # Calculate the RSI based on EWMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    RS3 = roll_up3 / roll_down3
    RSI3 = 100.0 - (100.0 / (1.0 + RS3))
    
    # Calculate the SMA
    roll_up4 = pd.rolling_mean(up2, 14)
    roll_down4 = pd.rolling_mean(down2.abs(), 14)
    roll_up5 = pd.rolling_mean(up3, 14)
    roll_down5 = pd.rolling_mean(down3.abs(), 14)

    # Calculate the RSI based on SMA
    RS4 = roll_up4 / roll_down4
    RSI4 = 100.0 - (100.0 / (1.0 + RS4))
    RS5 = roll_up5 / roll_down5
    RSI5 = 100.0 - (100.0 / (1.0 + RS5))
    
    plt.figure()
    RSI2.plot()
    RSI3.plot()
    RSI4.plot()
    RSI5.plot()
    plt.title("Relative Strength Index")
    plt.legend(['RSI Stock1 via EWMA', 'RSI Stock2 via EWMA', 'RSI Stock1 via SMA', 'RSI Stock2 via SMA'])
    plt.show()
    

def MACD(data1):
    data1['26 EMA'] = pd.ewma(data1['Close'],span=26)
    data1['12 EMA'] = pd.ewma(data1['Close'],span=12)
    data1['MACD'] = data1['26 EMA'] - data1['12 EMA']
    data1.plot(y=['MACD'],title='MACD')
    plt.title("Moving Avg. Convergence Divergence")
    plt.show()
    plt.legend(['MACD'])
    
def MACD_CSA(data2,data3):
    data2['26 EMA'] = pd.ewma(data2['Close'],span=26)
    data2['12 EMA'] = pd.ewma(data2['Close'],span=12)
    data2['MACD'] = data2['26 EMA'] - data2['12 EMA']
    data3['26 EMA'] = pd.ewma(data3['Close'],span=26)
    data3['12 EMA'] = pd.ewma(data3['Close'],span=12)
    data3['MACD'] = data3['26 EMA'] - data3['12 EMA']
    data2['MACD'].plot()
    data3['MACD'].plot()
    plt.title("Moving Avg. Convergence Divergence")
    plt.legend(['MACD Stock1', 'MACD Stock2'])
    plt.show()
    

def BollBands(data1):
    data1['30 Day MA'] = data1['Close'].rolling(window = 20).mean()
    data1['30 Day STD'] = data1['Close'].rolling(window = 20).std()
    data1['Upper Band'] = data1['30 Day MA'] + (data1['30 Day STD'] * 2)
    data1['Lower Band'] = data1['30 Day MA'] - (data1['30 Day STD'] * 2)
    data1[['Upper Band','Lower Band','Close','30 Day MA']].plot(figsize=(12,6))
    plt.title("Bollinger Bands")
    plt.show()
    plt.legend()

def BollBands_CSA(data2,data3):
    data2['30 Day MA'] = data2['Close'].rolling(window = 20).mean()
    data2['30 Day STD'] = data2['Close'].rolling(window = 20).std()
    data2['Upper Band'] = data2['30 Day MA'] + (data2['30 Day STD'] * 2)
    data2['Lower Band'] = data2['30 Day MA'] - (data2['30 Day STD'] * 2)
    data3['30 Day MA'] = data3['Close'].rolling(window = 20).mean()
    data3['30 Day STD'] = data3['Close'].rolling(window = 20).std()
    data3['Upper Band'] = data3['30 Day MA'] + (data3['30 Day STD'] * 2)
    data3['Lower Band'] = data3['30 Day MA'] - (data3['30 Day STD'] * 2)
    data2[['Upper Band','Lower Band','Close','30 Day MA']].plot()
    data3[['Upper Band','Lower Band','Close','30 Day MA']].plot()
    #plt.legend(["Bollinger Bands Stock1", "Bollinger Bands Stock2"])
    plt.legend()
    plt.show()


def MA(data1):
    data1['14 Day Moving Average'] = data1['Close'].rolling(window = 14).mean()
    data1['7 Day Moving Average'] = data1['Close'].rolling(window = 7).mean()
    data1[['14 Day Moving Average','7 Day Moving Average']].plot(figsize=(12,6))
    plt.title("Price Change")
    plt.show()
    plt.legend()

def MA_CSA(data2,data3):
    data2['14 Day Moving Average'] = data2['Close'].rolling(window = 14).mean()
    data2['7 Day Moving Average'] = data2['Close'].rolling(window = 7).mean()
    data3['14 Day Moving Average'] = data3['Close'].rolling(window = 14).mean()
    data3['7 Day Moving Average'] = data3['Close'].rolling(window = 7).mean()
    data2['14 Day Moving Average'].plot()
    data2['7 Day Moving Average'].plot()
    data3['14 Day Moving Average'].plot()
    data3['7 Day Moving Average'].plot()
    plt.title("Price Change")
    plt.legend(['14 Day Moving Avg Stock1', '7 Day Moving Avg Stock1', '14 Day Moving Avg Stock2', '7 Day Moving Avg Stock2'])
    plt.show()

fullname1=StringVar()
email1=StringVar()
password1 = StringVar()
number1=StringVar()
bandb1= StringVar()
ctype1 = StringVar()
cnumber1 = StringVar()
nameoncard1 = StringVar()

def database():
    fullname = fullname1.get()
    email = email1.get()
    password = password1.get()
    number = number1.get()
    bandb = bandb1.get()
    ctype = ctype1.get()
    cnumber = cnumber1.get()
    nameoncard = nameoncard1.get()
    emailf = 0
    passwordf = 0
    numberf = 0
    ctypef = 0
    cnumberf = 0
    if("@" in email and "." in email):
        emailf = 1
    if(len(password) >= 8 and len(password)<=12):
        passwordf = 1
    if(len(number)==10 and number.isnumeric()):
        numberf = 1
    if(ctype=='Debit' or ctype=='Credit' or ctype=='credit' or ctype=='debit' or ctype=='DEBIT' or ctype=='CREDIT'):
        ctypef = 1
    if(len(cnumber)==16):
        cnumberf = 1
    if(emailf == 1 and passwordf == 1 and numberf == 1 and ctypef == 1 and cnumberf == 1):
        conn = sqlite3.connect('Form.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS UserDB(fullname TEXT, email TEXT, password TEXT, number TEXT, bandb TEXT, ctype TEXT, cnumber TEXT, nameoncard TEXT)')
            cursor.execute('INSERT INTO UserDB(fullname,email,password,number,bandb,ctype,cnumber,nameoncard) VALUES(?,?,?,?,?,?,?,?)',(fullname,email,password,number,bandb,ctype,cnumber,nameoncard))
        conn.commit()
    else:
        if(emailf==0):
            tkinter.messagebox.showinfo('Recheck','Invalid Email')
        if(passwordf==0):
            tkinter.messagebox.showinfo('Recheck','Invalid Password')
        if(numberf==0):
            tkinter.messagebox.showinfo('Recheck','Invalid Contact Number')
        if(ctypef==0):
            tkinter.messagebox.showinfo('Recheck','Invalid Card Type')
        if(cnumberf == 0):
            tkinter.messagebox.showinfo('Recheck','Invalid Card Number')
        
        
email2 = StringVar()
password2 = StringVar()
def login():
    conn = sqlite3.connect("Form.db")
    email3 = email2.get()
    password3 = password2.get()
    with conn:
        cursor = conn.cursor()
    sqlq = cursor.execute("SELECT COUNT(1) FROM UserDB where email="+'"'+email3+'"'+" and password = "+'"'+password3+'";')
    if sqlq.fetchone()[0]:
        postlogin_window()
    else:
        answer=tkinter.messagebox.askquestion('Login Error','Incorrect Email ID or password. Create New User ID?')
        if answer == 'yes':
            signup_window()
        else:
            login_window()
    conn.commit()

def login_window():
    window = tk.Toplevel(win)
    window.title("Login")
    window.geometry("380x120")
    
    Label(window,text="  Enter Email ID",font=("Times",13)).place(x=30,y=15)
    ef1=Entry(window,textvar=email2)
    ef1.place(x=200,y=15)
    Label(window,text="  Enter Password",font=("Times",13)).place(x=30,y=45)
    ef2=Entry(window,show="*",textvar=password2)
    ef2.place(x=200,y=45)
    submit=Button(window,text="Submit",command=lambda:[window.destroy(),login()],bg="firebrick",fg="white",font=("Times",13))
    submit.place(x=160,y=80)
    
def postlogin_window():
    window = tk.Toplevel(win)
    window.title("Stock Management")
    window.geometry("550x210")
    
    l=Label(window,text="Select one of the following options",font=("Times",15))
    l.place(x=140,y=25)
    buy=Button(window,text="Buy",command=buy_stock_window,font=("Times",13),bg="lightskyblue3",fg="black",height=3,width=15)
    buy.place(x=50,y=70)
    sell=Button(window,text="Sell",command=sell_stock_window,font=("Times",13),bg="lightskyblue3",fg="black",height=3,width=15)
    sell.place(x=200,y=70)
    manage=Button(window,text="Manage",font=("Times",13),bg="lightskyblue3",fg="black",height=3,width=15)
    manage.place(x=350,y=70)
    lo=Button(window,text="Logout",command=window.destroy,font=("Times",13),bg="firebrick4",fg="white",height=1,width=7)
    lo.place(x=235,y=170)

def buy_stock_window():
    window = tk.Toplevel(win)
    window.title("Buy Stock")
    window.geometry("380x155")
    
    Label(window,text="Enter name of stock",font=("Times",13)).place(x=30,y=15)
    ef1=Entry(window)
    ef1.place(x=200,y=15)
    Label(window,text="Enter quantity",font=("Times",13)).place(x=30,y=45)
    ef2=Entry(window)
    ef2.place(x=200,y=45)
    Label(window,text="Enter CVV",font=("Times",13)).place(x=30,y=75)
    ef3=Entry(window,show="*")
    ef3.place(x=200,y=75)
    submit=Button(window,text="Buy",bg="firebrick",fg="white",font=("Times",13),height=1,width=6)
    submit.place(x=160,y=115)

def sell_stock_window():
    window = tk.Toplevel(win)
    window.title("Sell Stock")
    window.geometry("380x120")
    
    Label(window,text="Enter name of stock",font=("Times",13)).place(x=30,y=15)
    ef1=Entry(window)
    ef1.place(x=200,y=15)
    Label(window,text="Enter quantity",font=("Times",13)).place(x=30,y=45)
    ef2=Entry(window)
    ef2.place(x=200,y=45)
    submit=Button(window,text="Sell",bg="firebrick",fg="white",font=("Times",13),height=1,width=6)
    submit.place(x=160,y=80)

def signup_window():
    window = tk.Toplevel(win)
    window.title("Sign-up")
    window.geometry("500x550")

    def entry_click1(event):
        if E3.get() == '8-12 characters':
           E3.delete(0, "end") # delete all the text in the entry
           E3.insert(0, '') #Insert blank for user input
           E3.config(fg = 'black')
    def entry_click2(event):
        if E4.get() == '10 digit mobile no':
           E4.delete(0, "end") # delete all the text in the entry
           E4.insert(0, '') #Insert blank for user input
           E4.config(fg = 'black')
    def entry_click3(event):
        if E6.get() == 'Credit or Debit':
           E6.delete(0, "end") # delete all the text in the entry
           E6.insert(0, '') #Insert blank for user input
           E6.config(fg = 'black')  
    def on_focusout(event):
        if E3.get() == '':
            E3.insert(0, '8-12 characters')
            E3.config(fg = 'grey')
        if E4.get() == '':
            E4.insert(0, '10 digit mobile no')
            E4.config(fg = 'grey')
        if E6.get() == '':
            E6.insert(0, 'Credit or Debit')
            E6.config(fg = 'grey')
    
    Label(window,text="Sign-up",font=("Times",20)).place(x=200,y=25)
    L1=Label(window,text="Full Name",font=("Times",13))
    L1.place(x=90,y=80)
    E1=Entry(window,textvar=fullname1)
    E1.place(x=260,y=80)
    L2=Label(window,text="Email ID",font=("Times",13))
    L2.place(x=90,y=130)
    E2=Entry(window,textvar=email1)
    E2.place(x=260,y=130)
    L3=Label(window,text="Password",font=("Times",13))
    L3.place(x=90,y=180)
    E3=Entry(window,textvar=password1)
    E3.insert(0,'8-12 characters')
    E3.bind('<FocusIn>',entry_click1)
    E3.bind('<FocusOut>',on_focusout)
    E3.config(fg='grey')
    E3.place(x=260,y=180)
    L4=Label(window,text="Contact Number",font=("Times",13))
    L4.place(x=90,y=230)
    E4=Entry(window,textvar=number1)
    E4.insert(0,'10 digit mobile no')
    E4.bind('<FocusIn>',entry_click2)
    E4.bind('<FocusOut>',on_focusout)
    E4.config(fg='grey')
    E4.place(x=260,y=230)
    L5=Label(window,text="Bank and Branch",font=("Times",13))
    L5.place(x=90,y=280)
    E5=Entry(window,textvar=bandb1)
    E5.place(x=260,y=280)
    L6=Label(window,text="Card Type",font=("Times",13))
    L6.place(x=90,y=330)
    E6=Entry(window,textvar=ctype1)
    E6.insert(0,'Credit or Debit')
    E6.bind('<FocusIn>',entry_click3)
    E6.bind('<FocusOut>',on_focusout)
    E6.config(fg='grey')
    E6.place(x=260,y=330)
    L7=Label(window,text="Card Number",font=("Times",13))
    L7.place(x=90,y=380)
    E7=Entry(window,textvar=cnumber1)
    E7.place(x=260,y=380)
    L8=Label(window,text="Name on Card",font=("Times",13))
    L8.place(x=90,y=430)
    E8=Entry(window,textvar=nameoncard1)
    E8.place(x=260,y=430)
    Button(window,text="Submit",command=lambda:[database(),window.destroy()],bg="firebrick",fg="white",font=("Times",14)).place(x=200,y=480)
    
def create_windowSSA(): 
    window = tk.Toplevel(win) 
    window.title("Single Stock Analysis")
    window.geometry("350x125")
    
    def on_entry_click(event):
        if ef2.get() == 'YYYY-MM-DD':
           ef2.delete(0, "end") # delete all the text in the entry
           ef2.insert(0, '') #Insert blank for user input
           ef2.config(fg = 'black')
    def on_entry_click2(event):
        if ef3.get() == 'YYYY-MM-DD':
           ef3.delete(0, "end") # delete all the text in the entry
           ef3.insert(0, '') #Insert blank for user input
           ef3.config(fg = 'black')   
    def on_focusout(event):
        if ef2.get() == '':
            ef2.insert(0, 'YYYY-MM-DD')
            ef2.config(fg = 'grey')
        if ef3.get() == '':
            ef3.insert(0, 'YYYY-MM-DD')
            ef3.config(fg = 'grey')
            
    Label(window,text="Enter name of stock",font=("Times",13)).place(x=20,y=5) 
    ef1=Entry(window) 
    ef1.place(x=200,y=5) 
    Label(window,text="Enter start date",font=("Times",13)).place(x=20,y=30)
    ef2=Entry(window)
    ef2.insert(0,'YYYY-MM-DD')
    ef2.bind('<FocusIn>',on_entry_click)
    ef2.bind('<FocusOut>',on_focusout)
    ef2.config(fg='grey')
    ef2.place(x=200,y=30)
    Label(window,text="Enter end date",font=("Times",13)).place(x=20,y=55)
    ef3=Entry(window)
    ef3.insert(0,'YYYY-MM-DD')
    ef3.bind('<FocusIn>',on_entry_click2)
    ef3.bind('<FocusOut>',on_focusout)
    ef3.config(fg='grey')
    ef3.place(x=200,y=55)
    submit=Button(window,text="Analyse",command=lambda:[create_WindowSubmitSSA(),retrieve_inputSSA(ef1,ef2,ef3),window.destroy()],bg="firebrick",fg="white",font=("Times",14)) 
    submit.place(x=140,y=85)
    
def retrieve_inputSSA(ef1,ef2,ef3): 
    global sname1 
    global sdate 
    global edate 
    global data1 
    sname1 = ef1.get() 
    sname1 = "NSE/"+sname1  
    sdate = ef2.get()   
    edate = ef3.get() 
    data1 = quandl.get(sname1, start_date = sdate, end_date = edate)
    
def create_WindowSubmitSSA():
    window=tk.Toplevel(win)
    window.title("Stock Indicators")
    window.geometry("500x300")
    
    Label(window,text="Select the indicator for analysis",font=("Times",13)).place(x=140,y=25)
    b1=Button(window,text="RSI",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20, command = lambda:[RSI(data1)])
    b1.place(x=55,y=55)
    b2=Button(window,text="MACD",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20,command=lambda:[MACD(data1)])
    b2.place(x=250,y=55)
    b3=Button(window,text="Bollinger Bands",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20,command=lambda:[BollBands(data1)])
    b3.place(x=55,y=150)
    b4=Button(window,text="Price Change",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20,command=lambda:[MA(data1)])
    b4.place(x=250,y=150)

def create_windowCSA():
    window = tk.Toplevel(win)
    window.title("Comparative Stock Analysis")
    window.geometry("390x150")
    
    def on_entry_click(event):
        if ef3.get() == 'YYYY-MM-DD':
           ef3.delete(0, "end") # delete all the text in the entry
           ef3.insert(0, '') #Insert blank for user input
           ef3.config(fg = 'black')
    def on_entry_click2(event):
        if ef4.get() == 'YYYY-MM-DD':
           ef4.delete(0, "end") # delete all the text in the entry
           ef4.insert(0, '') #Insert blank for user input
           ef4.config(fg = 'black')   
    def on_focusout(event):
        if ef3.get() == '':
            ef3.insert(0, 'YYYY-MM-DD')
            ef3.config(fg = 'grey')
        if ef4.get() == '':
            ef4.insert(0, 'YYYY-MM-DD')
            ef4.config(fg = 'grey')
            
    Label(window,text="Enter name of first stock",font=("Times",13)).place(x=20,y=5)
    ef1=Entry(window)
    ef1.place(x=240,y=5)
    Label(window,text="Enter name of second stock",font=("Times",13)).place(x=20,y=30)
    ef2=Entry(window)
    ef2.place(x=240,y=30)
    Label(window,text="Enter start date",font=("Times",13)).place(x=20,y=55)
    ef3=Entry(window)
    ef3.insert(0,'YYYY-MM-DD')
    ef3.bind('<FocusIn>',on_entry_click)
    ef3.bind('<FocusOut>',on_focusout)
    ef3.config(fg='grey')
    ef3.place(x=240,y=55)
    Label(window,text="Enter end date",font=("Times",13)).place(x=20,y=80)
    ef4=Entry(window)
    ef4.insert(0,'YYYY-MM-DD')
    ef4.bind('<FocusIn>',on_entry_click2)
    ef4.bind('<FocusOut>',on_focusout)
    ef4.config(fg='grey')
    ef4.place(x=240,y=80)
    submit=Button(window,text="Analyse",command=lambda:[create_WindowSubmitCSA(),retrieve_inputCSA(ef1,ef2,ef3,ef4),window.destroy()],bg="firebrick",fg="white",font=("Times",14))
    submit.place(x=160,y=110)

def retrieve_inputCSA(ef1,ef2,ef3,ef4): 
    global sname2
    global sname3
    global sdate1 
    global edate1 
    global data2
    global data3
    sname2 = ef1.get() 
    sname2 = "NSE/"+sname2
    sname3 = ef2.get()
    sname3 = "NSE/"+sname3
    sdate1 = ef3.get()   
    edate1 = ef4.get() 
    data2 = quandl.get(sname2, start_date = sdate1, end_date = edate1)
    data3 = quandl.get(sname3, start_date = sdate1, end_date = edate1)

def create_WindowSubmitCSA():
    window=tk.Toplevel(win)
    window.title("Stock Indicators")
    window.geometry("500x300")
    
    Label(window,text="Select the indicator for analysis",font=("Times",13)).place(x=140,y=25)
    b1=Button(window,text="RSI",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20, command = lambda:[RSI_CSA(data2,data3)])
    b1.place(x=55,y=55)
    b2=Button(window,text="MACD",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20,command=lambda:[MACD_CSA(data2,data3)])
    b2.place(x=250,y=55)
    b3=Button(window,text="Bollinger Bands",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20,command=lambda:[BollBands_CSA(data2,data3)])
    b3.place(x=55,y=150)
    b4=Button(window,text="Price Change",font=("Times",13),bg="lightskyblue3",fg="black",height=4,width=20,command=lambda:[MA_CSA(data2,data3)])
    b4.place(x=250,y=150)

def analysis_window():
    window= tk.Toplevel(win)
    window.title("Stock Analysis")
    window.geometry("500x500")

    Label(window,text="Select the type of analysis to be done",font=("Times",15)).place(x=115,y=115)
    SSA= Button(window,text="Single Stock Analysis",command=create_windowSSA,height=4,width=25,bg="royalblue3",fg="white",font=("Times",13))
    SSA.place(x=140,y=160)
    CSA= Button(window,text="Comparative Stock Analysis",command=create_windowCSA,height=4,width=25,bg="royalblue3",fg="white",font=("Times",13))
    CSA.place(x=140,y=265)    

Label(win,text="Welcome to the Stock Management and Analysis System",font=("Times",15)).place(x=25,y=70)

Login=Button(win,text="Login",command=login_window,height=4,width=25,font=("Times",13),bg="royalblue3",fg="white")
Login.place(x=130,y=120)

Signup=Button(win,text="Sign-up",command=signup_window,height=4,width=25,font=("Times",13),bg="royalblue3",fg="white")
Signup.place(x=130,y=220)

Analyse=Button(win,text="Analyse",command=analysis_window,height=4,width=25,font=("Times",13),bg="royalblue3",fg="white")
Analyse.place(x=130,y=320)


win.mainloop()
