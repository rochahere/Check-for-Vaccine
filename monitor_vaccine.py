

from selenium import webdriver  # Opens the explorer to get the info
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup # Parse webpage info
import time # Makes script to wait while page loads
import smtplib # Send email notification
from secrets import * # Imports your secret information


while True:
  # Selenium Chrome Driver
  browser = webdriver.Chrome('chromedriver')
  # URL to be check
  browser.get('https://vaccinatelaredo.timetap.com/#/')
  # Let the page load for 3 seconds
  time.sleep(3)
  # Save web info in variable
  html_source = browser.page_source  
  # Close driver
  browser.quit()
  # Parse html data
  soup = BeautifulSoup(html_source,'html.parser')
  # Find needed html tag
  findID = soup.find("div",{"id":"welcomeText"})  
  # Look for text (if vaccine is available or not)
  if "NOW FULL" in str(findID):
    print("Not Available")
    # Waits 60 seconds to run script againg
    time.sleep(60)
    # Keeps script running
    continue

  else:
    # Create email message with just a subject line,
    msg = 'Vaccine Available'
    # Set the 'from' address,
    fromaddr = your_email
    # Set the 'to' addresses,
    toaddrs  = [to_email]
    
    # Setup the email server,
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Add my account login name and password,
    server.login(your_email, your_pass)

    # Send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # Disconnect from the server
    server.quit()
    # Ends while
    break
