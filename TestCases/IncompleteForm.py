from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://jupiter.cloud.planittesting.com/#/')
# Click on 'Contact'
driver.find_element_by_id('nav-contact').click()
time.sleep(2)

# Fill in form incompletely
driver.find_element_by_id('forename').send_keys('Joseph')
driver.find_element_by_id('surname').send_keys('Joestar')
driver.find_element_by_id('email').send_keys('Hermit@.com')
driver.find_element_by_id('message').click()

# Submit feedback
driver.find_element_by_link_text('Submit').click()
print("Error messages:")
print(driver.find_element_by_id('email-err').text)
print(driver.find_element_by_id('message-err').text)
print(driver.find_element_by_class_name('alert-error').text)

# Success Message with ILLEGAL format
driver.find_element_by_id('message').send_keys('/\w+@[A-Za-z0-9]+.[A-Za-z]{2,}/')
driver.find_element_by_link_text('Submit').click()
driver.implicitly_wait(5)
print("Submit with invalid email in feedback:")
print(driver.find_element_by_class_name('alert-success').text)

time.sleep(2)
driver.quit()
