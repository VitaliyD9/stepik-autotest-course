from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value").text
    print(x_element)
    y = calc(x_element)

    form = browser.find_element_by_css_selector("input[id=answer]")
    form.send_keys(y)
    option1 = browser.find_element_by_css_selector("input[id=robotCheckbox]")
    option1.click()
    option2 = browser.find_element_by_css_selector("input[id=robotsRule]").click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(3)
    browser.quit()
