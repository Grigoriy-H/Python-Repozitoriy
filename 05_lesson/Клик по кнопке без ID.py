from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера

# Запуск веб-драйвера с использованием Service и ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("http://uitestingplayground.com/dynamicid")         # Шаг 1: Открытие страницы

# Шаг 2: Клик на синюю кнопку
try:

    button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]")))

    button.click()  # Кликаем на кнопку

    print("Кнопка успешно нажата.")

finally:         # Закрытие браузера
    driver.quit()