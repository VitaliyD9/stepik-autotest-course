from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button1 = browser.find_element_by_id("book")
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()

    element_x = browser.find_element_by_id("input_value").text
    x = str(math.log(abs(12 * math.sin(int(element_x)))))

    input = browser.find_element_by_id("answer")
    input.send_keys(x)

    button2 = browser.find_element_by_id("solve")
    button2.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)



finally:
    browser.quit()