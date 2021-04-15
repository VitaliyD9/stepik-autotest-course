from selenium import webdriver
import math

default_link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(default_link)

link = browser.find_element_by_link_text(text)
link.click()




