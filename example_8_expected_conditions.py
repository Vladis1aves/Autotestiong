from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
#Неявное ожидание
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

#Явное ожидание
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
#или
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
)
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

"https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions"
#Обратите внимание, что в объекте WebDriverWait используется функция until, в которую передается правило ожидания, элемент, а также значение, по которому мы будем искать элемент. В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

# Ожидание проверки наличия оповещения в данный момент и переключения на него.
switch_to_alert = WebDriverWait(browser, 5).until(EC.alert_is_present())

# Ожидание того, что все из нескольких ожидаемых условий верны.
# Эквивалент логического «И». Возвращает: Если какое-либо ExpectedCondition не выполнено: False. Когда все ExpectedConditions выполнены: список с возвращаемым значением каждого ExpectedCondition
# .all_of(*expected_conditions: Callable[[WebDriver], Literal[False] | T]) → Callable[[WebDriver], List[T] | Literal[False]]
expected_conditions = []
all_of = WebDriverWait(browser, 5).until(EC.all_of(*expected_conditions))

#Ожидание того, что любое из нескольких ожидаемых условий истинно.
# Эквивалент логического «ИЛИ». Возвращает результаты первого условия соответствия или False, если ни одно из них не соответствует.
# .any_of(*expected_conditions: Callable[[WebDriver], T]) → Callable[[WebDriver], Literal[False] | T]
any_of = WebDriverWait(browser, 5).until(EC.any_of(*expected_conditions))


# Ожидание проверки того, включен ли данный атрибут в указанный элемент.
# локатор, атрибут
# .element_attribute_to_include(locator: Tuple[str, str], attribute_: str) → Callable[[WebDriver], bool]
element_attribute_to_include =  WebDriverWait(browser, 5).until(EC.element_attribute_to_include(locator, attribute))

# Ожидание найти элемент и проверить, находится ли указанное состояние выбора в этом состоянии.
# locator is a tuple of (by, path) is_selected is a boolean
# .element_located_selection_state_to_be(locator: Tuple[str, str], is_selected: bool) → Callable[[WebDriver], bool]
element_located_selection = WebDriverWait(browser, 5).until(EC.element_located_selection_state_to_be(locator, bool))






title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present