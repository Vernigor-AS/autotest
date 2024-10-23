import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#функция для расчета из задачи
def calc(a, b):
    return str(a + b)

try:
    #запуск браузера
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    #поиск текста и перевод в целое число
    treasure_element1 = browser.find_element(By.CSS_SELECTOR, value='#num1')
    a = int(treasure_element1.text)
    treasure_element2 = browser.find_element(By.CSS_SELECTOR, value='#num2')
    b = int(treasure_element2.text)
    #вызов функции
    n = calc(a, b)
    #выбор из выпадающего списка нужной суммы
    select_dropdown = Select(browser.find_element(By.CSS_SELECTOR, value='#dropdown'))
    select_dropdown.select_by_visible_text(n)
    #поиск клик по кнопке
    button = browser.find_element(By.CSS_SELECTOR, value='[type="submit"]')
    button.click()

finally:
    time.sleep(3)
    browser.quit()
