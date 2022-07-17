from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://jupiter.cloud.planittesting.com/#/')
# Click on 'Shop'
driver.find_element_by_id('nav-shop').click()
time.sleep(2)
# Add each to cart
for i in driver.find_elements_by_class_name('btn-success'):
    i.click()
time.sleep(2)
driver.quit()
