import unittest
from selenium import webdriver
import time

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)


class TestSelectors(unittest.TestCase):
    def test_link_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('div.first_block input.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block input.third")
        input3.send_keys("IvanPetrov@mail.mail")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected_text = "Congratulations! You have successfully registered!"
        
        self.assertEqual(expected_text, welcome_text, f"expected {expected_text}, got {welcome_text}")
        
    def test_link_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('div.first_block input.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block input.third")
        input3.send_keys("IvanPetrov@mail.mail")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(expected_text, welcome_text, f"expected {expected_text}, got {welcome_text}")
        
if __name__ == "__main__":
    unittest.main()