from selenium import webdriver
import time

default_link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(default_link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Vitaliy")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Dushkin")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Novosibirsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Czech")
    button = browser.find_element_by_xpath('.//button[@type="submit"]')
    button.click()

finally:
    time.sleep(9)
    browser.quit()
