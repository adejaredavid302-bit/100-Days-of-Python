import os
from twilio.rest import Client
from smtplib import SMTP
class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_email(self, message_body):
        my_email = "adejaredavid302@gmail.com"
        password = os.environ["YOUR_APP_PASSWORD"]

        with smtp.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(my_email, password)
            server.sendmail(my_email ")

