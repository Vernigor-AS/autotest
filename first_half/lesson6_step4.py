from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #запуск браузера
    link = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск ссылки по частичному тексу и клик по ней
    target_link = browser.find_element(By.PARTIAL_LINK_TEXT, value="224592")
    target_link.click()
    #заполнение полей ввода регистрации
    input1 = browser.find_element(By.TAG_NAME, value='input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value='last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value='form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value="country")
    input4.send_keys("Russia")
    #поиск и нажатие кпопки "регистрация"
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

