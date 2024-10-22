from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #запуск браузера
    link = 'http://suninjuly.github.io/huge_form.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск полей ввода
    elements = browser.find_elements(By.TAG_NAME, value='input')
    #ввести во все поля ввода "Hello"
    for element in elements:
        element.send_keys("Hello")
    #поиск кнопки и клик по ней
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    #время ожидания чтобы скопировать код
    time.sleep(15)
    #закрытие браузера
    browser.quit()



