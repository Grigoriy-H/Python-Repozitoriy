import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from online_store_page import Online_Store_Page  # Импортируем класс страницы


@pytest.fixture(scope="module")                              
def driver():                                                # Запуск Chrome-драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_for_an_online_store(driver):                          # Создали страницу магазина
    online_store_page = Online_Store_Page(driver)

    online_store_page.open("https://www.saucedemo.com/")       # Открываем сайт магазина

    online_store_page.login("standard_user", "secret_sauce")   # Авторизация

    online_store_page.add_items_to_cart()                      # Добавление товаров в корзину

    online_store_page.go_to_cart()                             # Переход в корзину

    online_store_page.checkout()                               # Нажимаем на кнопку Checkout

    online_store_page.fill_checkout_form("Иван", "Петров", "123456")  # Заполняем форму для оформления

    total_value = online_store_page.get_total_price()          # Получаем итоговую сумму

                                                               # Проверяем итоговую сумму
    assert total_value == "58.29", (f"Expected total to be $58.29, but got ${total_value}. ""Проверьте итоговую сумму в корзине.")