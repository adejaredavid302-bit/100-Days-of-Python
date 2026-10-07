import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Day_50_TinDog_Automation_Bot.main import login_btn

load_dotenv()
SIMILAR_ACCOUNT=""
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")
BASE_URL="https://app.100daysofpython.dev/services/share-a-naan/welcome"
LOGIN_URL=f"{BASE_URL}/login"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)
        wait = WebDriverWait(self.driver, 10)
        login_botton=self.driver.find_element(By.CSS_SELECTOR, ".naan-btn-primary")
        login_botton.click()
        email_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        email_login.send_keys(USERNAME)
        password_login = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_login.send_keys(PASSWORD)
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        save_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".naan-popup-dismiss")))
        save_login.click()
        notification = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.naan-popup-card .naan-popup-dismiss")))
        notification.click()

    def find_followers(self):
        pass
    def follow(self):
        pass
bot=InstaFollower()
bot.login()