from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")

print(driver.title)
sleep(5)
driver.quit()
