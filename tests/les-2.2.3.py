from re import X
import os
from xml.dom.minidom import Element
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполняем поля
    input_name = browser.find_element_by_xpath("//input[@placeholder='Enter first name']").send_keys("Тестовое Имя")
    input_name = browser.find_element_by_xpath("//input[@placeholder='Enter last name']").send_keys("Тестовое Фамилия")
    input_name = browser.find_element_by_xpath("//input[@placeholder='Enter email']").send_keys("Тестовое Email")
    

    # добавляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_css_selector("#file").send_keys(file_path)
    element.send_keys(file_path)

    # Жмакаем на кнопку Submit
    button = browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()