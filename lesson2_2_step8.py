import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    #запуск браузера
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск и заполнение полей
    first_name = browser.find_element(By.CSS_SELECTOR, value='[placeholder="Enter first name"]')
    first_name.send_keys('Antony')
    last_name = browser.find_element(By.CSS_SELECTOR, value='[placeholder="Enter last name"]')
    last_name.send_keys('Ver')
    email = browser.find_element(By.CSS_SELECTOR, value="[placeholder='Enter email']")
    email.send_keys('1sav1@gmail.com')
    #путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    #поиск кнопки и загрузка файла на страницу
    element = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    element.send_keys(file_path)
    #поиск кнопки и клик по ней
    button = browser.find_element(By.CSS_SELECTOR, value='[type="submit"]')
    button.click()

finally:
    #ожидание, что все выполнено успешно и закрытие браузера
    time.sleep(10)
    browser.quit()