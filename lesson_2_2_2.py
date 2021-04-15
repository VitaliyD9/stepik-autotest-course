from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    #вычислили значение
    element_x = browser.find_element_by_id("input_value").text
    x = str(math.log(abs(12*math.sin(int(element_x)))))
    print(element_x)
    #заполнили поле
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(x)
    #выбрали чекбокс
    checkbox = browser.find_element_by_id("robotCheckbox").click()

    #нашли кнопку и проскролили страницу
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #нажали радиобаттон
    radio_button = browser.find_element_by_id("robotsRule").click()

    #нажали на кнопку
    button.click()

finally:
    time.sleep(9)
    browser.quit()