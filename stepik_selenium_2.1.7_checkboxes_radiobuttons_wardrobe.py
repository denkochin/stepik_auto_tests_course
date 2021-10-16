from selenium import webdriver
import time
import math

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# Код
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)


time.sleep(1)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
time.sleep(1)
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click() 
time.sleep(1)
option1 = browser.find_element_by_css_selector("#robotsRule")
option1.click() 
time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()