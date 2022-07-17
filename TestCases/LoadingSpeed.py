# python 3.7
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://jupiter.cloud.planittesting.com/#/')
# Get loading time
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendTime = responseStart - navigationStart
frontendTime = domComplete - responseStart

print("Back End loaded in %s ms." % backendTime)
print("Front End loaded in %s ms" % frontendTime)

driver.quit()
