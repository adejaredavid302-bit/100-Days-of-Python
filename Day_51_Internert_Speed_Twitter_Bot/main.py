import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
PROMISED_DOWN = 1000
PROMISED_UP = 2000
Y_EMAIL = os.getenv('Y_EMAIL')
Y_PASSWORD = os.getenv('Y_PASSWORD')
Y_LOGIN = os.getenv('Y_LOGIN')

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.Up = 0
        self.Down = 0
        self.wait = WebDriverWait(self.driver, 60)

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")
        short_wait = WebDriverWait(self.driver, 10)
        cookie_button = short_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']")))
        self.driver.execute_script("arguments[0].click();", cookie_button)
        sleep(2)
        go_button = short_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_button.click()
        print("Speed test running... waiting for final data...")
        self.Down = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.download-speed"))).text
        self.Up = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.upload-speed"))).text

        print(f"Actual Download: {self.Down} Mbps")
        print(f"Actual Upload: {self.Up} Mbps")
    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN)
        short_wait = WebDriverWait(self.driver, 10)
        if float(self.Down) < PROMISED_DOWN or float(self.Up) < PROMISED_UP:
            print("Speeds are slow! Initiating automated complaint procedure...")
            email_field = short_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
            email_field.send_keys(Y_EMAIL)
            password_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            password_field.send_keys(Y_PASSWORD)
            login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_btn.click()
            short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".public-DraftEditor-content")))
            complaint_msg = (f"Hey Internet Provider, why is my speed {self.Down} Down / {self.Up} Up "
                f"when I pay for {PROMISED_DOWN} Down / {PROMISED_UP} Up?")
            tweet_input = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftEditor-content")
            tweet_input.send_keys(complaint_msg)
            submit_post_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn-tweet")
            submit_post_btn.click()
            print("Complaint post has been successfully dispatched!")
        else:
            print("Network matches contract agreements. Script closing safely.")
Tweet_bot = InternetSpeedTwitterBot()
Tweet_bot.get_internet_speed()
Tweet_bot.tweet_at_provider()
