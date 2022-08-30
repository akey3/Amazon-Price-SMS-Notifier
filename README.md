# Amazon-Price-SMS-Notifier
This program will notify the user daily if the price of the selected product drops. 
* The program uses Selenium to scrape the webpage for the price by finding it's XPATH.
* If the price is lower than it was the day before, the program utilizes the twilio library to send an SMS text message to the user's personal cell phone. ![amazon](https://user-images.githubusercontent.com/68174547/187545567-0df618f0-f310-4259-84f0-3cb797f80edb.png)
