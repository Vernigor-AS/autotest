from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    #запуск браузера
    link = "http://suninjuly.github.io/wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #ожидание когда кнопка станет активной и клик по ней
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    #ожидание появление сообщения и сравнение текста 
    message = browser.find_element(By.ID, "verify_message")
    time.sleep(5)
    assert "successful" in message.text

finally:
    browser.quit()