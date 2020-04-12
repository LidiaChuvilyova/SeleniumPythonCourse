from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
    return math.log(math.fabs(12 * math.sin(x)))

link =  "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element_by_id("book")
    text = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button.click()

    x = browser.find_element_by_id("input_value").text
    res = calc(int(x))
    print(res)
    input = browser.find_element_by_id("answer")
    input.send_keys(str(res))

    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла