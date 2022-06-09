from re import X
import os
from xml.dom.minidom import Element
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

   # Жмакаем на кнопку
    button = browser.find_element_by_xpath("//button[@type='submit']").click()

    # Подтверждаем
    confirm = browser.switch_to.alert
    confirm.accept()

    # Посчитаем
    def calc(x): return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Жмакаем на кнопку Submit
    button3 = browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()