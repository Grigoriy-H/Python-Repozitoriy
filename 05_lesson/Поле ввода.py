from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service

from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager  # Подключаем менеджер драйвера

from time import sleep

# Настройка опций Firefox (без указания пути к Firefox)
options = Options()

# Запуск Firefox-драйвера с использованием Service и GeckoDriverManager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

try:
    #  Открытие страницы
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    # Ввод текста "1000"
    input_field.send_keys("1000")
    sleep(5)

    # Очистка поля ввода
    input_field.clear()
    sleep(3)

    # Ввод текста "999"
    input_field.send_keys("999")
    sleep(5)

    print("Скрипт выполнен успешно.")



finally:
    # Закрытие браузера
    driver.quit()