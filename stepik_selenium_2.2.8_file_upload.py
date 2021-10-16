from selenium import webdriver
import time
import os

# Строки, которые нужно добавлять, чтобы не возникало ошибки в Chrome
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# Initialise link variable.
link = "http://suninjuly.github.io/file_input.html"
# Get HTML-code from the link.
browser.get(link)

# Find First name input box and put the value into it
input_first_name = browser.find_element_by_css_selector("input[name='firstname']")
input_first_name.send_keys("Name")

# Find Last name input box and put the value into it
input_last_name = browser.find_element_by_css_selector("input[name='lastname']")
input_last_name.send_keys("Surname")

# Find Email input box and put the value into it
input_email = browser.find_element_by_css_selector("input[name='email']")
input_email.send_keys("email@domain.com")

# Prepare the path of the file to upload
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

# Find the upload button and send the file path to it
file_upload = browser.find_element_by_css_selector("input#file")
file_upload.send_keys(file_path)

# Click "Submit" button
submit_button = browser.find_element_by_css_selector("button.btn")
submit_button.click()
time.sleep(5)

# Close the browser with killing it's proccesses
browser.quit()