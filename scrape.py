import requests
from bs4 import BeautifulSoup
import smtplib
URL = input("Enter a link : ")
while "https://www.newegg.ca/" not in URL:
    print("Please enter a valid link")
    URL = input("Enter a link : ")
SuggestedPrice = input("Please enter a price to watch for : ")

#URL = "https://www.newegg.ca/p/34-725-086"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

def priceCheck():
    webpage = requests.get(URL, headers = headers) 
    soup = BeautifulSoup(webpage.content, "html.parser")
    Product = soup.find(class_="product-title").get_text()
    cost = soup.find(class_="price-current").get_text()
    rounded = cost[1:-3]
    rounded = rounded.replace(',','')
    roundedPrice = float(rounded)

    if (roundedPrice < int(SuggestedPrice)):
        sendMail()
        print(Product.strip())
        print(cost.strip())
        
def sendMail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("Fakespamemail22@gmail.com", "789123gG+")
    subject = "price drop!"
    body = "The Price has Dropped! Here is the Link : ", URL
    message = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        "Fakespamemail22@gmail.com",
        "Fakespamemail22@gmail.com",
        message
    )
    print("EMAIL SENT")
    server.quit()

priceCheck()
