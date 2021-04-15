from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is None

    button = browser.find_element_by_css_selector("button.btn")
    button_checked = button.get_attribute("disabled")
    print("value of button disabled attribute: ", button_checked)
    assert button_checked is None

    time.sleep(10)
    button_checked = button.get_attribute("disabled")
    print("value of button disabled attribute after 10 sec: ", button_checked)
    assert button_checked is not None


finally:
    browser.quit()
