from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# Код
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Click on non-visible button and get an ElementClickInterceptedException
# button = browser.find_element_by_tag_name("button")
# button.click()

# Write a js-script that scrolls the page till the button is visible, then execute it and click the button
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()