from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



try:
    #запуск браузера
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск и заполнение полей ввода
    input1 = browser.find_element(By.TAG_NAME, value='input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value='last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value='form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value="country")
    input4.send_keys("Russia")
    #поиск и клик кнопки
    button = browser.find_element(By.XPATH, value="//button[text()='Submit']")
    button.click()

finally:
    #ожидание чтобы скопировать код
    time.sleep(15)
    #закрытие браузера
    browser.quit()

