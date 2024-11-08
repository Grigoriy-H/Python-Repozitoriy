from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера

# Запуск веб-драйвера с использованием Service и ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


    # Открытие страницы
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(20)
driver.find_element(By.LINK_TEXT, "Добавить элемент").click()



driver.quit()