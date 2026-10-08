import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import  ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()
SIMILAR_ACCOUNT = "elaineducasse"
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan/welcome"
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)
        wait = WebDriverWait(self.driver, 10)
        login_botton = self.driver.find_element(By.CSS_SELECTOR, ".naan-btn-primary")
        login_botton.click()
        email_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        email_login.clear()
        email_login.send_keys(USERNAME)
        password_login = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_login.clear()
        password_login.send_keys(PASSWORD)
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        save_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".naan-popup-dismiss")))
        save_login.click()
        notification = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.naan-popup-dismiss")))
        notification.click()

    def find_followers(self):
        wait = WebDriverWait(self.driver, 10)
        search_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-naan-search-toggle]")))
        search_btn.click()
        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "aside div input")))
        search_input.send_keys(SIMILAR_ACCOUNT)
        search_input.send_keys(Keys.ENTER)
        followers_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers")))
        followers_link.click()
        print("Followers list opened!...")
        modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.followers-scroll")))
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", modal)
            sleep(2)
        print("Scrolling complete! Followers list fully generated.")

    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, ".naan-follower-row")
        for follower in followers:
            try:
                follow_btn = follower.find_element(By.CSS_SELECTOR, ".naan-follow-btn")
                follow_btn.click()
                sleep(2)
            except ElementClickInterceptedException:
                print("USER FOLLOWED")
                cancel_btn = self.driver.find_element(By.CSS_SELECTOR, ".naan-unfollow-cancel")
                cancel_btn.click()
                sleep(2)
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()