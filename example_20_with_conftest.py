from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    login = browser.find_element(By.CSS_SELECTOR, "#ember35")
    login.click()
    email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    email.send_keys("email")
    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.send_keys("password")
    button = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
    button.click()
    time.sleep(30)

