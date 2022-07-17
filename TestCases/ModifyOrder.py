from selenium import webdriver
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
# Change Quantity
driver.find_element_by_class_name('input-mini').send_keys(10)
time.sleep(1)
# Remove Item
driver.find_element_by_class_name('remove-item').click()
time.sleep(1)
driver.find_element_by_link_text('Yes').click()
time.sleep(1)
# Back to shopping
driver.find_element_by_partial_link_text('Start').click()
time.sleep(2)
driver.quit()
