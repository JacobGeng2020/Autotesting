from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://jupiter.cloud.planittesting.com/#/')
# Click on 'Shop'
driver.find_element_by_id('nav-shop').click()
time.sleep(2)
# Add one item to cart
driver.find_element_by_class_name('btn-success').click()
time.sleep(2)
# Click 'Cart'
driver.find_element_by_id('nav-cart').click()
time.sleep(1)
# Head to check out
driver.find_element_by_partial_link_text('Check').click()
time.sleep(1)
# Fill in form with wrong email
driver.find_element_by_id('forename').send_keys('Joseph')
driver.find_element_by_id('surname').send_keys('Joestar')
email = driver.find_element_by_id('email')
email.send_keys('H@.com')
driver.find_element_by_id('address').send_keys('Liverpool, England')
card = driver.find_element_by_id('cardType')
select_card = Select(card)
select_card.select_by_value('Visa')
# select_card.select_by_visible_text('MasterCard')
driver.find_element_by_id('card').send_keys('abcd')
driver.find_element_by_id('checkout-submit-btn').click()
# Error Message
print(driver.find_element_by_id('email-err').text)
print(driver.find_element_by_class_name('alert-error').text)
#email.clear()
#email.send_keys('H@P.com')
#driver.find_element_by_id('checkout-submit-btn').click()
time.sleep(5)
# Order success Message with wrong details
print(driver.find_element_by_class_name('alert-success').text)
time.sleep(2)
driver.quit()
