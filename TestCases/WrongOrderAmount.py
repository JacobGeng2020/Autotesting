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
Quantity = driver.find_element_by_class_name('input-mini')
Quantity.send_keys('1111111111111111111111111111111')
time.sleep(1)
print("Status of cart and total after put in a ridiculous number:")
print(driver.find_element_by_id('nav-cart').text)
print(driver.find_element_by_class_name('total').text)

# Check out
driver.find_element_by_partial_link_text('Check').click()
time.sleep(1)

# Wrong amount
print("Amount in Check Out page:")
print(driver.find_element_by_id('header-message').text)

# 'Null Cart'
driver.find_element_by_id('nav-cart').click()
Quantity = driver.find_element_by_class_name('input-mini')
Quantity.clear()
Quantity.send_keys('00')
print("Status of cart after put in '00':")
print(driver.find_element_by_id('nav-cart').text)
time.sleep(2)
driver.quit()
