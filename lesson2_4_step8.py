import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.wait import WebDriverWait
#функция для расчета из задачи
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #запуск браузера
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #ожидание пока цена не изменится до $100 и клик по кнопке
    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100')
    )
    button_1 = browser.find_element(By.CSS_SELECTOR, value='#book')
    button_1.click()
    #поиск текста и вызов функции для расчета (текст в формуле переведется в целое число)
    x_element = browser.find_element(By.CSS_SELECTOR, value='#input_value').text
    answer = calc(x_element)
    #поиск поля ввод и ввод данных
    answer_input = browser.find_element(By.CSS_SELECTOR, value='#answer')
    answer_input.send_keys(answer)
    #поиск кнопки и клик по ней
    button_2 = browser.find_element(By.CSS_SELECTOR, value='#solve')
    button_2.click()

finally:

    time.sleep(10)
    browser.quit()