from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)


driver.get("http://uitestingplayground.com/ajax")          # Открыть сайт


button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ajaxButton')))

button.click()                # Нажать на синюю кнопку

try:

    WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success')))

    green_text_element = driver.find_element(By.CSS_SELECTOR, 'p.bg-success')

    if green_text_element.is_displayed():
       
       green_text = green_text_element.text

       print("Данные, загруженные с помощью запроса на получение AJAX.", green_text)

    else:

        print("Data not loaded.", "Данные не загружены.")

except TimeoutException:

    print("Timed out.","время ожидания истекло.")


driver.quit()                      # Закрываем браузер
