from re import X
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Присвоим значение для первого числа
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    x=int(x)

    # Присвоим значение для второго числа
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    y=int(y)


    # Расчитываем значение по формуле
    z = str(x + y)
    
    # Работаем с выпадашкой
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(z)
    
    # Жмакаем на кнопку
    button = browser.find_element_by_css_selector("button[type='submit']").click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла