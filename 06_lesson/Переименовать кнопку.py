from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)


driver.get("http://uitestingplayground.com/textinput")     # Открываем  сайт


input_field = WebDriverWait(driver, 15). until(EC.presence_of_element_located((By.CSS_SELECTOR, '#newButtonName')))

input_field.send_keys("SkyPro")     #  В поисковую строку вводим текст "SkyPro.""


search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#updatingButton')))

search_button.click()                # Нажимаем  кнопку



try:
   # время ожидания до 20 секунд 
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#updatingButton'), "SkyPro"))
    
    element_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
   
    if element_text.is_displayed():
        new_text = element_text.text 
    
    print(new_text)
    

except TimeoutException:

    print("Кнопка не переименована.")


driver.quit()                           # Закрыть веб-драйвер