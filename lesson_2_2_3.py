from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    print(file_path)
    field_first_name = browser.find_element_by_css_selector("input.form-control")
    field_first_name.send_keys("Vitaliy")
    field_last_name = browser.find_element_by_name("lastname")
    field_last_name.send_keys("Dushkin")
    field_email = browser.find_element_by_name("email")
    field_email.send_keys("test@test.ru")
    file_load = browser.find_element_by_id("file")
    file_load.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(9)
    browser.quit()