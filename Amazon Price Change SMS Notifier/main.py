from selenium import webdriver
from twilio.rest import Client
import time

def get_driver():
# Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863FR3S9/?th=1")
  return driver

def main():
  driver = get_driver()
  # xpath was taken in Chrome by right-clicking
  # over <span aria-hidden="true">$15.12</span>
  # and then Copy -> xpath
  element = driver.find_element(by="xpath", value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
  return element.text

def clean_price(raw):
  return float(raw.replace('$', ''))

account_sid ='AC03bb93eb4fbdc226da8ec697726cd551'
auth_token = '5466abcb7ae96142db31bda38ecaca90'
client = Client(account_sid, auth_token)


raw_price= main()
price = clean_price(raw_price)

prices = [price]

while True: 
  # 86400 seconds allows the program to run once a day :)
  time.sleep(86400)
  raw_price= main()
  price = clean_price(raw_price)
  prices.append(price)
  print(prices)
  
  if prices[-1] < prices[-2]:
    message = client.messages.create(
                  body=f"The price has just dropped to ${price}. Hurry up!",
                  # twilio number goes in the "from"
                  from_='+00000',
                  # personal cell number goes in the "to"
                  to='+00000'
                  )
  # delete the latest price in the list 
  del prices[-2]
  
  
  
