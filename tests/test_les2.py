from cgitb import text
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from re import X
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestBookPage():
    def keys_to_typing (self, browser, link):
        link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(link)
        input = browser.find_element(By.XPATH, "//textarea")
        x = str(math.log(int(time.time())))
        input.sendkeys(x)
        # Добавляем ожидание
        button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()

   

if __name__ == "__main__": pytest.main()


    # 1. Копируем фикстуру браузера из пред. шага

# 2.Создаем фикстуру параметриз('переменная', ["урлы"])

# 3. Создаем класс, название с Test..

# 4. Создаем функцию, название с test...(селф, браузер, переменная с шага 2)

# 5. Создаем переменную = str(math.log(int(time.time())))

# 6. link = переменная 2 шага; браузер гет(link)

# 7. Добавляем ожидание

# 8. Находим поле для ввода ответа и send_keys туда переменную с 5 шага (можно и сразу ввести, не создавая переменную)

# 9. Находим кнопку Отправить через  WebDriverWait...   EC.element_to_be_clickable (так как она не сразу доступна) и нажимаем на нее ( либо после шага 8 - добавьте ожидание)

# 10. Создаем переменную селектора правильности ответа: просто откройте любой урл из списка, введите что угодно в поле и нажмите копку (неважно что неправильный ответ - селектор тот же), после ищите его в коде

# 11. Ассерт 'правильный ответ' in переменная селектора правильности. text

# 12. В конце иф нейм = мейн:

#                              пайтест.мейн()