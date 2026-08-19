import requests
import datetime
import smtplib
import time
MY_LAT=51.507351
MY_LONG=-0.127758
my_email = "adejaredavid302@gmail.com"
password = "YOUR_APP_PASSWORD"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_latitude=float(data["iss_position"]["latitude"])
    iss_longitude=float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night_overhead():
    parameter = {"lat": MY_LAT,
                 "lng": MY_LONG,
                 "formatted":0}
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["result"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["result"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
            return True
while True:
    time.sleep(60)
    is_night_overhead()
    if is_iss_overhead() and is_night_overhead():
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(my_email,password)
        server.sendmail(from_addr=my_email,to_addrs="adejaredavid302@gmail.com",
                            msg="Subject:Lookup\n\nThe iss is in the sky")
