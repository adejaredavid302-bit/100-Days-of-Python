from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
FORM_URL="https://forms.gle/et2ZNoro3TAroa1B6"


URL="https://appbrewery.github.io/Zillow-Clone/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL,headers = HEADERS)
soup=BeautifulSoup(response.text,"html.parser")
price_tags = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
all_price=[item.text.split("/")[0].split("+")[0] for item in price_tags]
#print(all_price)
addresses=soup.select('address[data-test="property-card-addr"]')
all_addresses=[item.text.strip() for item in addresses]
#print(all_addresses)
links=soup.find_all('a',class_="property-card-link")
all_links=[item.get("href") for item in links]
# print(all_links)

class DateEntry:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
    def fill_data(self):
        for i in range(len(all_addresses)):
            self.driver.get(FORM_URL)
            self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"input[type='text']")))
            form_fill=self.driver.find_elements(By.CSS_SELECTOR,"input[type='text']")
            form_fill[0].send_keys(all_addresses[i])
            form_fill[1].send_keys(all_price[i])
            form_fill[2].send_keys(all_links[i])
            submit_button=self.driver.find_element(By.CSS_SELECTOR,"span[class='NPEfkd']")
            submit_button.click()
            print(f"Property entry {i + 1}/{len(all_addresses)} successfully submitted.")
            sleep(2)
        print("Data entry pipeline complete! You can safely close the window.")
bot=DateEntry()
bot.fill_data()