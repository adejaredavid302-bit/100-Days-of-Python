from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

PROMISED_DOWN=1000
PROMISED_UP=2000
Y_EMAIL=os.getenv('Y_EMAIL')
Y_PASSWORD=os.getenv('Y_PASSWORD')
Y_LOGIN=os.getenv('Y_LOGIN')

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome(options=chrome_options)
        self.Up=0
        self.Down=0
        self.wait=WebDriverWait(self.driver,60)
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))).click()
        self.Down = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.download-speed"))).text
        self.Up = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.upload-speed"))).text
        print(f"Actual Download: {self.Down}")
        print(f"Actual Upload: {self.Up}")

    def tweet_at_provider(self):
        pass


Tweet_bot=InternetSpeedTwitterBot()
Tweet_bot.get_internet_speed()
