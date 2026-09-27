from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
cookie_button=driver.find_element(By.ID,"bigCookie")
language_button=driver.find_element(By.CLASS_NAME,"langSelectButton title")
for cookie in range(0,1000):
    cookie_button.send_keys(Keys.ENTER)








