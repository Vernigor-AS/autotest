import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    #запуск браузера
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    #ожидание появления искомого элемента
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#input_value')))
    #считывание искомого элемента в виде текста, перевод текста в целое число и последующий расчет
    x = browser.find_element(By.CSS_SELECTOR, value='#input_value').text
    x = int(x)
    answer = str(math.log(abs(12 * math.sin(x))))
    #поиск поля ввода, скролл для видимости, ввод ответа
    input1 = browser.find_element(By.CSS_SELECTOR, value='#answer')
    browser.execute_script("arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(answer)
    #поиск и клик чекбокса и радиокнопки
    checkbox = browser.find_element(By.CSS_SELECTOR, value='#robotCheckbox')
    checkbox.click()
    radio_button = browser.find_element(By.CSS_SELECTOR, value='#robotsRule')
    radio_button.click()
    # кнопка перекрыта, прокрутка страницы пока элемент не станет видимым
    submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
    # выравнивание элемента и клик по нему
    browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", submit)
    browser.execute_script("arguments[0].click();", submit)

finally:
    time.sleep(15)
    browser.quit()