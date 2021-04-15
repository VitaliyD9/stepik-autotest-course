from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    input1 = browser.find_element_by_css_selector('input.first:required')
    input1.send_keys("Vitaliy")
    input2 = browser.find_element_by_css_selector('input.second:required')
    input2.send_keys("Dushkin")
    input3 = browser.find_element_by_css_selector('input.third:required')
    input3.send_keys("qwe@test.ru")

# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
    time.sleep(1)

# находим элемент, содержащий текст
    welcome_text_elm = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elm.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert  "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
