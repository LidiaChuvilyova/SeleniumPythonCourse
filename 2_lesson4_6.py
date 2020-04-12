from selenium import webdriver
import time 
import math

def calc(x):
    return math.log(math.fabs(12 * math.sin(x)))

link =  "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла