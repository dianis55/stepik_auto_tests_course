from re import X
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Расчитываем значение по формуле
    def calc(x): return str(math.log(abs(12*math.sin(int(x)))))
    
    # Находим изображение с сундуком по CSS селектору
    x_element = browser.find_element_by_css_selector("#treasure")
    
    # Возвращаем атрибут элемента
    x= x_element.get_attribute("valuex")
    y = calc(x)

    # Вводим ответ в поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Жмакаем на чекбокс
    button = browser.find_element_by_css_selector("#robotCheckbox").click()

    # Жмакаем на радиобаттон
    button = browser.find_element_by_css_selector("#robotsRule").click()

    # Жмакаем на кнопку
    button = browser.find_element_by_css_selector("button[type='submit']").click()
     

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла