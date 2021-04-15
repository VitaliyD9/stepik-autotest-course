from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    print(x)
    y = browser.find_element_by_id("num2").text
    print(y)
    sum = str(int(x) + int(y))
    print(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(9)
    browser.quit()
