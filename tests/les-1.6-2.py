from re import X
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    X=str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element_by_link_text(X)
    link.click()

    input1 = browser.find_element_by_css_selector("div:nth-child(1) > input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div:nth-child(2) > input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div:nth-child(3) > input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла