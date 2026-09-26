import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

URL="https://appbrewery.github.io/instant_pot/"
HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:156.0) Gecko/20100101 Firefox/156.0",
        "Accept-Language":"en-US,en;q=0.9"}
webpage=requests.get(URL,headers=HEADERS)
soup=BeautifulSoup(webpage.text,"html.parser")
webpage_price=soup.find(name="span",class_="aok-offscreen")
price=float(webpage_price.getText().split("$")[1])
web_product=soup.find(name="h1",class_="a-size-large a-spacing-none")
web_product_text=web_product.getText()

SENDER_EMAIL=os.getenv("MAIL")
SENDER_PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL =input("Enter receiver email:").lower()
SUBJECT ="From ADEJARE"
MESSAGE=f"{SUBJECT}:\n\n {web_product_text} {price} {URL}"

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        MESSAGE = MESSAGE.encode("ascii", "ignore").decode("ascii")
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)