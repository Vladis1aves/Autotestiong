from selenium.webdriver.common.by import By
import time
import math
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TestLink1():
    @pytest.mark.parametrize("link",
                             [
                                 "https://stepik.org/lesson/236895/step/1"
                                 # ,
                                 # "https://stepik.org/lesson/236896/step/1",
                                 # "https://stepik.org/lesson/236897/step/1",
                                 # "https://stepik.org/lesson/236898/step/1",
                                 # "https://stepik.org/lesson/236899/step/1",
                                 # "https://stepik.org/lesson/236903/step/1",
                                 # "https://stepik.org/lesson/236904/step/1",
                                 # "https://stepik.org/lesson/236905/step/1"
                             ]
                             )
    def test_login_link_1(self, browser, link):
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        login = browser.find_element(By.CSS_SELECTOR, "#ember35")
        login.click()
        email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        email.send_keys("email")
        password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        password.send_keys("password")
        button = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
        button.click()
        # time.sleep(15)
        # ember96
        # ember93
        input_ = browser.find_element(By.CSS_SELECTOR, "#ember93")
        input_ = WebDriverWait(browser, 5).until(EC.element_located_selection_state_to_be(input_, True))
        answer = math.log(int(time.time()))
        input_.send_keys(answer)
        time.sleep(10)
        button_send = browser.find_element(By.CSS_SELECTOR, "#ember79 > div > section > div > div.attempt__inner > div.attempt__actions > button")
        button_send = WebDriverWait(browser, 7).until(EC.element_to_be_clickable(button_send))
        button_send.click()
        time.sleep(30)
        message = browser.find_element(By.CSS_SELECTOR, "#ember99 > p")
        assert "Correct!" is message.text
