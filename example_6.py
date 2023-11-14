
alert = browser.switch_to.alert
#Cоглашаемся с алертом
#Для конфирма
alert.accept()
#Получаем текст алерта
alert_text = alert.text
#Отменяем конфирм
confirm.dismiss()
#Промпт окна
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()