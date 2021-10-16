from selenium import webdriver
import time
from math import log, sin

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# Initialise link variable.
link = "http://suninjuly.github.io/execute_script.html"
# Get HTML-code from the link.
browser.get(link)

# Read the x value
x = int(browser.find_element_by_tag_name("span#input_value").text)

# Calculate the function on the page
formula = str(log(abs(12 * sin(x))))

# Find input box, scroll till it's visible and put the value into it
input_box = browser.find_element_by_tag_name("input#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_box) 
input_box.send_keys(formula)

# Check "I'm the robot"
checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
checkbox.click()

# Switch radio to "Robots rule"
radio = browser.find_element_by_css_selector("input#robotsRule")
radio.click()

# Click "Submit" button
submit_button = browser.find_element_by_css_selector("button.btn")
submit_button.click()
time.sleep(5)

# Close the browser with killing it's proccesses
browser.quit()