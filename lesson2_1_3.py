from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # получаем скрытое значение
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    print(x)
    # высчитываем значение по формуле
    y = calc(x)
    # вставляем значение в поле
    form = browser.find_element_by_css_selector('input[id="answer"]')
    form.send_keys(y)
    # отмечаем чекбокс
    option1 = browser.find_element_by_id("robotCheckbox").click()
    # отмечаем радиобаттон
    option2 = browser.find_element_by_id("robotsRule").click()
    # жмем кнопку
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(9)
    browser.quit()
