import pytest
from selenium import webdriver

# Декоратор, который означает, что функция возвращает объект для всех функций-тестов, 
# куда мы передадим его в качестве аргумента
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Декоратор, создающий параметр "language" со списком значений.
# Тест запустится с каждым значением отдельно.
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

# Декоратор, создающий параметр "language" со списком значений.
# Каждый тест класса запустится с каждым значением отдельно.
@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        print("test_guest_should_see_navbar_element")
        # этот тест тоже запустится дважды