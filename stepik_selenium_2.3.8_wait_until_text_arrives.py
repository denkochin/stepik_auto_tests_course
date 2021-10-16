from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import log, sin

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
book_condition = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
book = browser.find_element_by_css_selector("button#book.btn.btn-primary")
book.click()

# Find x value tag, pick the text from it and convert to int
x = int(browser.find_element_by_tag_name("span#input_value.nowrap").text)

# Calculate the formula with x value and convert it to str
formula = str(log(abs(12 * sin(x))))

# Find input box and send formula result to it
input_formula = browser.find_element_by_css_selector("input#answer.form-control")
input_formula.send_keys(formula)

# Click "Submit" button
submit_button = browser.find_element_by_css_selector("button#solve.btn.btn-primary")
submit_button.click()
time.sleep(5)

# Close the browser with killing it's proccesses
browser.quit()
