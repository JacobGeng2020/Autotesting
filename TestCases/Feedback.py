from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://jupiter.cloud.planittesting.com/#/')
# Click on 'Contact'
driver.find_element_by_id('nav-contact').click()
time.sleep(2)

# Fill in form
driver.find_element_by_id('forename').send_keys('Joseph')
driver.find_element_by_id('surname').send_keys('Joestar')
driver.find_element_by_id('email').send_keys('Hermit@Purple.com')
driver.find_element_by_id('message').send_keys('/\w+@[A-Za-z0-9]+.[A-Za-z]{2,}/')

# Submit feedback
driver.find_element_by_link_text('Submit').click()
driver.implicitly_wait(5)

# Success Message with legal format
print(driver.find_element_by_class_name('alert-success').text)

time.sleep(2)
driver.quit()
