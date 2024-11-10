from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from webdriver_manager.chrome import ChromeDriverManager  

from time import sleep


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)


driver.get("http://uitestingplayground.com/classattr")  # Шаг 1: Открытие страницы
sleep(5)

try:
  
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))  # Ищем по CSS
                                             
    button.click()  # Кликаем на кнопку     
    print("Кнопка нажата.")

finally:
    
    driver.quit()                             # Закрытие браузера