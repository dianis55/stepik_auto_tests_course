from re import X
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Присвоим значение для первого числа
    def calc(x): return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Жмакаем на чекбокс
    button = browser.find_element_by_css_selector("#robotCheckbox").click()
    
    # Скроллим окно на 150 пикселей вниз
    browser.execute_script("window.scrollBy(0, 150);")

    # Жмакаем на радиобаттон
    button2 = browser.find_element_by_css_selector("#robotsRule").click()

    # Жмакаем на кнопку Submit
    button3 = browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла