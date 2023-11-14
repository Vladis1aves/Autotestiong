from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(20)
browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(y)
submit = browser.find_element(By.CSS_SELECTOR, "#solve")
submit.click()
time.sleep(10)
browser.close()

# В этом уроке мы постарались собрать ссылки на ресурсы, где вы сможете найти дополнительную информацию по использованию Selenium и о тонкостях при работе с ним:
#
# Общее
#
# http://chromedriver.chromium.org/getting-started﻿
# ﻿https://www.guru99.com/selenium-tutorial.html — ﻿Туториал на английском, ориентирован на Java.﻿
# https://www.guru99.com/live-selenium-project.html — ﻿Можно попробовать писать автотесты для демо-сайта ﻿банка. Тоже Java.
# http://barancev.github.io/good-locators/ — что такое хорошие селекторы
# http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная?
# Ожидания в Selenium WebDriver
#
# https://www.selenium.dev/documentation/webdriver/waits/﻿﻿
# https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
# https://blog.codeship.com/get-selenium-to-wait-for-page-load/
# http://barancev.github.io/slow-loading-pages/
# http://barancev.github.io/page-loading-complete/
