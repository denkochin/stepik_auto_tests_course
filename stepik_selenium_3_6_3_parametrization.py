import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print("\nstart browser for test..")
    global browser
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()

link = "https://stepik.org/lesson/236895/step/1"

class TestAliens():
    result = ""
    lessons = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ]

    @pytest.mark.parametrize('lesson', lessons)
    def test_case(self, browser, lesson):
        link = lesson
        browser.get("https://stepik.org/lesson/236905/step/1")
        textarea = browser.find_element(By.TAG_NAME, "textarea")
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)
        button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button.click()
        time.sleep(5)

'''
from selenium import webdriver
import pytest
import time
import math

final = ''


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()
    print(final)  # напечатать ответ про Сов в конце всей сессии


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой
'''

'''
import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"

    # Открываем ссылку
    browser.get(link)

    # Рассчитываем значение для ответа, переводим его тут же в строку
    answer = str(math.log(int(time.time())))

    # Ждем, что поле ввода отображается на странице и вводим туда рассчитанное значение
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea'))).send_keys(answer)

    # Нажимаем Отправить для проверки ответа
    browser.find_element_by_class_name('submit-submission').click()

    # Ждем фидбек
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'attempt-message_correct')))

    # Считываем текст из опционального фидбека
    optional_feedback = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text

    # Сравниваем этот текст с ожидаемым 'Correct'
    assert optional_feedback == 'Correct!', f"Expected 'Correct', received: {optional_feedback}"
'''