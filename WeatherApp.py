# Utilizing webscrapping
# Installing beautifulsoup4, requests, pillow

import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/d4b29f82c033911b5d17e57be2dfcf81a40f132d23d69c633add22fae9a16a6d"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open("/Users/stu/Practice Projects/weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--2_osB").text
    temperature = soup.find('span',class_="CurrentConditions--tempValue--1RYJJ").text
    weatherPrediction = soup.find('div',class_="CurrentConditions--phraseValue--17s79").text
    
    locationLabel.config(text = location)
    tempLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPrediction)

locationLabel = Label(master,font=("Calibri bold",20),bg = "white")
locationLabel.grid(row=0,sticky="N",padx=100)

tempLabel = Label(master,font=("Calibri bold",70),bg = "white")
tempLabel.grid(row=1,sticky="W",padx=40)
Label(master, image = img, bg = "white").grid(row=1,sticky="E")
weatherPredictionLabel = Label(master,font=("Calibri bold",15),bg="white")
weatherPredictionLabel.grid(row=2,sticky="W",padx=40)

getWeather()
master.mainloop()