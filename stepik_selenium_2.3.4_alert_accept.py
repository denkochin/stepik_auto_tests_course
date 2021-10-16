from selenium import webdriver
import time
from math import log, sin

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# Initialise link variable.
link = "http://suninjuly.github.io/alert_accept.html"
# Get HTML-code from the link.
browser.get(link)

# Find button and click it
button1 = browser.find_element_by_css_selector("button.btn.btn-primary")
button1.click()

# Switch to "confirm" alert and accept() it
confirm = browser.switch_to.alert
confirm.accept()

# Find x value tag, pick the text from it and convert to int
x = int(browser.find_element_by_tag_name("span#input_value.nowrap").text)

# Calculate the formula with x value and convert it to str
formula = str(log(abs(12 * sin(x))))

# Find input box and send formula result to it
input_formula = browser.find_element_by_css_selector("input#answer.form-control")
input_formula.send_keys(formula)

# Click "Submit" button
submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
submit_button.click()
time.sleep(5)

# Close the browser with killing it's proccesses
browser.quit()