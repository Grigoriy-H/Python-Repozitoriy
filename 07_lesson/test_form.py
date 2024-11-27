import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from text_form_page import TextFormPage  # Импорт класса страницы


@pytest.fixture(scope="module")  # Используем scope="module" для оптимизации

def driver():                    # Запуск Chrome-драйвер
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()                      


def test_form(driver):           # Создал объект страницы
    text_form_page = TextFormPage(driver)

                                 # Открыли  страницу с формой
    text_form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем поля форму
    text_form_page.fill_form(
        first_name='Иван',
        last_name='Петров',
        address='Ленина, 55-3',
        email='test@skypro.com',
        phone='+7985899998787',
        zip_code='',
        city='Москва',
        country='Россия',
        job_position='QA',
        company='SkyPro'
    )

    # Отправляем форму
    text_form_page.submit_form()

    # Ожидаем появления всех предупреждений
    text_form_page.wait_for_alerts()

    # Получаем все элементы предупреждений
    alerts = text_form_page.get_alerts()

    # Проверяем предупреждения
    try:
        text_form_page.check_alerts(alerts)
    except AssertionError as e:
        pytest.fail(f"Ошибка при проверке предупреждений: {str(e)}")
