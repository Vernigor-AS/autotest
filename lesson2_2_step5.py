import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
#функция расчета из задачи
def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    #запуск браузера
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск и клик по кнопке
    button = browser.find_element(By.CSS_SELECTOR, value="[type='submit']")
    button.click()
    #переключение на другую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #поиск текста
    x_element = browser.find_element(By.CSS_SELECTOR, value="#input_value").text
    #перевод текста в целое число
    a_element = int(x_element)
    #вызов фунции calc
    answer = calc(a_element)
    #поиск и ввод в поле посчитанных данных
    input_1 = browser.find_element(By.CSS_SELECTOR, value='#answer')
    input_1.send_keys(str((answer)))
    #поиск и клик по кнопке
    button = browser.find_element(By.CSS_SELECTOR, value='.btn.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

