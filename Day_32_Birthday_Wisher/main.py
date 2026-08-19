import smtplib
import datetime
import pandas
import random


date = datetime.datetime.now()
month = date.month
day = date.day
today = (month, day)

read_file = pandas.read_csv("birthdays.csv")

birthday_dict = {(row["month"], row["day"]): row.to_dict()for (index, row) in read_file.iterrows()}

if today in birthday_dict:
    random_letter = random.randint(1, 3)
    birthday_person = birthday_dict[today]
    with open(f"./letter_templates/letter_{random_letter}.txt","r") as letter_file:
        content = letter_file.read()

    birthday_letter = content.replace("[NAME]", birthday_person["name"])
    my_email = "adejaredavid302@gmail.com"
    password = "YOUR_APP_PASSWORD"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(my_email, password)
        server.sendmail(my_email, birthday_person["email"],f"Subject: Happy Birthday!\n\n{birthday_letter}")
