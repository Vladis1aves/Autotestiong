import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
#Decorator mark name test

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# pytest -s -v -m smoke test_fixture8.py  запуск с выбранной маркировкой
# Регистрация маркироков в файле pytest.ini
# Допустимы логические операторы в имени маркировки or not and
# Метка которая скипает тест, регистрировать не надо @pytest.mark.skip
# Метка для падающего теста @pytest.mark.xfail(reason="fixing this bug right now").
# Отличительная особенность: статус будет всегда положительный и меняться в зависимости от результата теста. К команде добавить -rx

