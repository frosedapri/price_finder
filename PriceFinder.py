import requests
from bs4 import BeautifulSoup
import smtplib
import time
import pickle
from tkinter import *
from tkinter import *
import os
from dateutil.tz import gettz
import datetime as dt




headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def check_price_Amazon():
    Amazon = pickle.load(open("Liens.dat", "rb"))
    #time=dt.datetime.now(gettz("Europe/Madrid")).isoformat()
    try:
        page = requests.get(Amazon, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
    #soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    

    #title = soup.find(id="productTitle").get_text()
        price = soup.find(id="priceblock_dealprice").get_text()
        converted_price = (price[0:4])
        print(converted_price)
        pickle.dump(converted_price, open("Prix.dat", "wb"))
        if(converted_price < prix):
            send_mail_Amazon()
    except Exception:
        try:
            page = requests.get(Amazon, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
    #soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    

    #title = soup.find(id="productTitle").get_text()
            price = soup.find(id="priceblock_ourprice").get_text()
            converted_price = (price[0:4])
            print(converted_price)


            if(converted_price < prix):
                send_mail_Amazon()
        except Exception:
            try:
                page = requests.get(Amazon, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
    #soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    

    #title = soup.find(id="productTitle").get_text()
                price = soup.find(id="priceblock_saleprice").get_text()
                converted_price = (price[0:4])
                print(converted_price)
                pickle.dump(URL_Amazon, open("Prix.dat", "wb"))
                pickle.dump(time, open("Prix.dat", "wb"))

                if(converted_price < prix):
                    send_mail_Amazon()
            except Exception:
                pass
    

def send_mail_Amazon():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bigfivepopo@gmail.com', '123456789!az')

    subject = 'price fell down on Amazon!'
    body = 'check the amazom link :' + URL_Amazon
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'bigfivepopo@gmail.com',
        'bigfivepopo@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit

#---------------------------------------------------------------------








while 1:
    check_price_Amazon()
