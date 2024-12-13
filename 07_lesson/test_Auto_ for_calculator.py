import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage  # Импортируем класс страницы


@pytest.fixture(scope="module")
def driver():                                                          # Запуск Chrome-драйвера 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_Auto_for_calculator(driver):                                   # Создаем объект страницы
    calculator_page = CalculatorPage(driver)

                                                                       # Открываем  страницу калькулятора
    calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

                                                                       # делаем задержку в 45 сек
    calculator_page.set_delay(45)

                                                                       # произведем вычисление
    calculator_page.calculate_sum()

                                                                       # Получим и проверим  результат 
    result_text = calculator_page.get_result()
    print(f"Результат вычислений: {result_text}")

    # Проверка результата
    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'."