from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.get(link)

# Ваш код, который заполняет обязательные поля
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
time.sleep(1)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
time.sleep(1)
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click() 
time.sleep(1)
option1 = browser.find_element_by_css_selector("[for='robotsRule']")
option1.click() 
time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()