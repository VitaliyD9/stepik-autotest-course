from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button1 = browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    element_x = browser.find_element_by_id("input_value").text
    x = str(math.log(abs(12 * math.sin(int(element_x)))))

    input = browser.find_element_by_id("answer")
    input.send_keys(x)
    button2 = browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')[-1]
    print(alert_text)


finally:
    browser.quit