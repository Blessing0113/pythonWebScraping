#!/usr/bin/env python
# coding: utf-8

# # AutoTrader Web Scraping

# In[1]:


from bs4 import BeautifulSoup
import requests
import datetime
import time

import smtplib


# In[2]:


url = "https://www.autotrader.co.za/car-for-sale/toyota/hilux/2.4gd-6/27465266?vf=2&db=1&s360=0&so=1&pl=1&pq=0&pr=3&po=1"



page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)


# In[3]:


Name = soup.find(class_ = "e-listing-title").get_text()
print(Name)


# In[4]:


price = soup.find(class_ = "e-price").get_text()
print(price)


# In[5]:


import csv

header = ["Name of Car", "Price", "Date"]

with open("CarNames.csv", "w") as F:
    F.write(",".join(header))
    


# In[6]:


Lists = [Name, price,date]

with open("CarNames.csv", "a+", newline = "", encoding = "UTF8") as F:

    writer = csv.writer(F)
    writer.writerow(Lists)
    


# In[8]:


p = price.strip()[2:]

string_price = p

print(string_price)


# In[9]:


import re

px = re.sub(r'\s+' , "", string_price)

print(px)


# In[10]:


results = int(px)
print(results)


# In[11]:


type(results)


# In[12]:


if results == 539800:
    print("Price is the same")
else:
    print("Still the same price")
    


# In[13]:





# In[7]:


date = datetime.date.today()

print(date)


# In[8]:


def checkCarPrice():
    url = "https://www.autotrader.co.za/car-for-sale/toyota/hilux/2.4gd-6/27465266?vf=2&db=1&s360=0&so=1&pl=1&pq=0&pr=3&po=1"



    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    
    Name = soup.find(class_ = "e-listing-title").get_text()
    
    price = soup.find(class_ = "e-price").get_text()
    
    header = ["Name of Car", "Price", "Date"]

    with open("CarNames.csv", "w") as F:
        F.write(",".join(header))
    
    
    Lists = [Name, price, str(date)]

    with open("CarNames.csv", "a+", newline = "", encoding = "UTF8") as F:
        F.write(",".join(header))
    #     F.write("\n")
        F.write(",".join(Lists))
        
        
    p = price.strip()[2:]

    string_price = p
    
    px = re.sub(r'\s+' , "", string_price)
    
    results = int(px)
    
    if results < 520000:
        send_mail()
#         print("You have got an discount")
#     else:
#         print("Still the same price")
    
    
    date = datetime.date.today()


# In[16]:


while (True):
    checkCarPrice()
    time.sleep(60)


# In[9]:


def send_email():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.ehlo()
    server.login("tshishongavhugala@gmail.com","vhug34")
    
    subject = "the car is below R520000"
    body = "HI! the chance you've been waiting for is HERE!"
    
    msg = f"Subject{subject}\n\n{body}"
    
    
    server.sendmail(
    "tshishongavhugala@gmail.com", msg)


# In[ ]:





# In[ ]:




