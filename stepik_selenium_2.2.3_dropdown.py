from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# Код
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

num1_tag = browser.find_element_by_css_selector("#num1")
num1 = num1_tag.text
num2_tag = browser.find_element_by_css_selector("#num2")
num2 = num2_tag.text
y = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1")  # ищет элемент с текстом "Python"
select.select_by_visible_text(str(y)) # ищет элемент по видимому тексту
# select.select_by_index(0)  # ищет элемент по его индексу или порядковому номеру (ндексация начинается с нуля)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()