from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import time,sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

language_button = driver.find_element(By.ID, "langSelect-EN")
sleep(15)
language_button.click()
print(f"You Selected {language_button.text}")

cookie_botton=driver.find_element(By.ID,"bigCookie")
cookie_botton_text=driver.find_element(By.ID,"cookies")
cookie_pre_seconds=driver.find_element(By.ID,"cookiesPerSeconds")

stop_time=time()+300
time_to_buy=time()+5
while True :
    cookie_botton.click()
    cookie_number=int(cookie_botton_text.text.split()[0].replace(",",""))
    to_be_purchased=None
    if time()>=time_to_buy:
        try:
            cookie_tools=driver.find_elements(By.CSS_SELECTOR,".product")
            for cookie in reversed(cookie_tools):
                price = cookie.find_element(By.CLASS_NAME, "price")
                if "enabled" in cookie.get_attribute("class"):
                    if int(price.text.replace(",", "")) <= cookie_number:
                        to_be_purchased=cookie
                        break

            if to_be_purchased:
                to_be_purchased.click()
                print(f"You Purchased:{to_be_purchased.get_attribute('id')}")

        except(NoSuchElementException,ValueError)as e:
            print(f"cookie not purchased\n REASON:{e}")
    if time()>=stop_time:
        print(f"Current cookies/sec{cookie_pre_seconds.text}")
        break