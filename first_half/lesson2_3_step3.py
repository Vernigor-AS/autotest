import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
#функция для расчета из задачи
def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) #просчет и возврат строки

try:
    #запуск браузера
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск кнопки и клик по ней
    button1 = browser.find_element(By.CSS_SELECTOR, value='.btn')
    button1.click()
    #нажатие кнопки в аллерте
    confirm = browser.switch_to.alert
    confirm.accept()
    #поиск элемента и вызов функции для расчета
    x_element = browser.find_element(By.CSS_SELECTOR, value='#input_value').text
    answer = calc(x_element)
    #поиск поля и ввод данных
    answer_input = browser.find_element(By.CSS_SELECTOR, value='#answer')
    answer_input.send_keys(answer)
    #поиск кнопки и клик по ней
    button2 = browser.find_element(By.CSS_SELECTOR, value='[type="submit"]')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()








