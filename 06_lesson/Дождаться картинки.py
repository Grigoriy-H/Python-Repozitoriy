from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager     # Подключаем менеджер драйвера



service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

try:
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")     # Открываем сайт

    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.ID, "text"), "Please wait until the images are loaded."))
    
    print("Текст 'Please wait until the images are loaded.' появился")


    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

    print("Текст поменялся на 'Done!'")

    
    try:
        image = driver.find_element(By.CSS_SELECTOR, '#award')       # Поиск изображения с ID "award"

        print("Изображение найдено:", image.get_attribute("src"))
    except Exception:  
    
        print("Изображение с ID 'award' не найдено.")

finally:
    
    driver.quit()                   # Закрываем драйвер