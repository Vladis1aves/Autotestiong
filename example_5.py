from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView"
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)
# browser.execute_script("window.scrollBy(0, 100);")