from selenium.webdriver.common.by import By
import time
import math
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLink1():
    @pytest.mark.parametrize("link",
                             [
                                 "https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"
                             ]
                             )
    def test_login_link_1(self, browser_chrome, link):
        browser = browser_chrome
        browser.get(link)
        login = browser.find_element(By.CSS_SELECTOR, "header nav a[href*='login']")
        login.click()
        email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        email.send_keys("email")
        password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        password.send_keys("password")
        button = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
        button.click()
        time.sleep(3)

        # again = browser.find_element(By.CSS_SELECTOR, "button[class*='again-btn']")
        # again.click()

        input_ = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='attempt'] textarea")))
        answer = math.log(int(time.time()))
        input_.send_keys(answer)
        button_send = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='attempt'] button")))
        button_send.click()
        message = browser.find_element(By.CSS_SELECTOR, "p[class*='smart-hints']")
        print(message.text)
        assert 'Correct!' in message.text, f"Incorrect message = {message.text}"

