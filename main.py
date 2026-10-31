# TODO 1: Get required data fro website
from bs4 import BeautifulSoup
import requests

scrapping_website_link = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=scrapping_website_link)

soup = BeautifulSoup(response.text, 'html.parser')

# Property Price
price_list = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
p_price = [price.getText().split("+")[0] for price in price_list]
property_price = [price.split("/")[0] for price in p_price]
print(len(property_price))

# Property Address
address_list = soup.find_all(name="address")
property_address = [address.getText().strip() for address in address_list]
print(len(property_address))

# Property link
link_list = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
property_link = [link.get("href") for link in link_list]
print(len(property_link))




# TODO 2: Using selenium fill Google form
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def fill_form(i):
    print(f"from number : {i}")
    Google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSdywNd87zJVgCbDWiPEhNFS8WIxaT65FS0NWgnK7ktRPouN1w/viewform?usp=header"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Google_form_link)
    time.sleep(2)

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(property_address[i])

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(property_price[i])

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(property_link[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    time.sleep(3)

    driver.quit()

print(property_address[43])
for i in range(44):
    fill_form(i=i)