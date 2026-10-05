from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
load_dotenv()

tinder_url = "https://app.100daysofpython.dev/services/tindog/u/hvCf_1jCxboK0t3kBFpJ5XWFdwhlsZFA"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(tinder_url)
wait = WebDriverWait(driver, 10)

main_window = driver.current_window_handle

login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tindog-cta-create")))
login_btn.click()
face_bark_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-facebark")))
face_bark_page.click()

wait.until(EC.number_of_windows_to_be(2))

for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#email")))
email.send_keys(os.getenv("EMAIL"))
password = driver.find_element(By.CSS_SELECTOR, "#pass")
password.send_keys(os.getenv("PASSWORD"))
face_bark_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
face_bark_login.click()

driver.switch_to.window(main_window)

locations = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.popup-card .btn-primary")))
locations.click()

popup_submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.popup-card button[type='submit']")))
popup_submit_btn.click()

accept_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form[method='post'] button[type='submit']")))
accept_btn.click()
while True:
    try:
        distance_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.distance")))
        tin_dog_location = distance_element.text
        cleaned_text = tin_dog_location.replace("km", "").replace("away", "").strip()
        distance = int(cleaned_text)
        print(f"Current dog profile distance: {distance} km")

        if distance == 1 or distance == 2:
            try:
                # Class selectors are cleaner using dot notation (button.btn-like)
                like_button = driver.find_element(By.CSS_SELECTOR, "button.btn-like")
                like_button.click()
                print("Swiped Right! ❤️")
            except ElementClickInterceptedException:
                print("Click Intercepted! Handling potential match screen...")
                try:
                    match_popup = driver.find_element(By.CSS_SELECTOR, ".match-popup a")
                    match_popup.click()
                    print("Dismissed Match Popup.")
                except NoSuchElementException:
                    sleep(2)
            except NoSuchElementException:
                sleep(2)
        else:
            dislike_button = driver.find_element(By.CSS_SELECTOR, "button.btn-nope")
            dislike_button.click()
            print("Swiped Left! 👎")
        sleep(1.5)
    except (TimeoutException, NoSuchElementException):
        print("Waiting for next profile card to load completely...")
        sleep(2)
