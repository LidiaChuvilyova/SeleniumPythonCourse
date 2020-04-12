from selenium import webdriver
import time 
import math

def calc(x):
    return math.log(math.fabs(12 * math.sin(x)))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type=\"submit\"]")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    res =  calc(int(x))
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