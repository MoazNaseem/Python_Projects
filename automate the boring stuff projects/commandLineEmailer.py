#! /usr/bin/python3
# commandLineEmailer.py takes and email address and
# a string and logs into your email account and sends 
# an email of the string to the provided address. 
 
from selenium import webdriver
import selenium.webdriver.support.ui as ui
# getting the details from the user.
email = input('Email Address: ')
subject = input('Subject: ')
message = input('Your message: ')

driver = webdriver.Firefox()
wait = ui.WebDriverWait(driver, 10)
driver.get('https://mail.yahoo.com')
emailElem = driver.find_element_by_id('login-username')
emailElem.clear()
emailElem.send_keys('awladnasem')
emailElem.submit()
wait.until(lambda driver: driver.find_element_by_id('login-passwd'))
passElem = driver.find_element_by_id('login-passwd')
passElem.clear()
passElem.send_keys('doublecork2')
driver.find_element_by_id('login-signin').click()
driver.find_element_by_link_text('Compose').click()
to = driver.find_element_by_id('message-to-field')
to.send_keys(email)
subElem = driver.find_element_by_tag_name('input[aria-label="Subject"]')
subElem.send_keys(subject)
messElem = driver.find_element_by_tag_name('div[aria-label="Message body"]')
messElem.send_keys(message)
driver.find_element_by_tag_name('button[title="Send this email"]').click()
driver.quit()

