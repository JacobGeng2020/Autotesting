from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://jupiter.cloud.planittesting.com/#/')
# Click on 'Login'
driver.find_element_by_id('nav-login').click()
# Type in account details
driver.find_element_by_id('loginUserName').send_keys('User')
driver.find_element_by_id('loginPassword').send_keys('Password')
# Click 'login'
time.sleep(2)
driver.find_element_by_class_name('btn-primary').click()
# Click 'cancel'
time.sleep(2)
driver.find_element_by_class_name('btn-cancel').click()
# Click 'logout'
# time.sleep(2)
# driver.find_element_by_id('nav-logout').click()
time.sleep(2)
driver.quit()
