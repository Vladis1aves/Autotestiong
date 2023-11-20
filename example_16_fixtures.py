import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# Допустимые значения установки области видимости для выполнения фикстуры:
# “function”, “class”, “module”, “session”
# @pytest.fixture(scope="class")
# Автоиспользование фикстур выглядит так:
# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # Ключевое слово, которое запустит выполнение дальнейшего кода,
    # после завершения функции, которая использовала фикстуру
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

