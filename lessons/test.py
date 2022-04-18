from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
)
browser.find_element(By.CSS_SELECTOR, '#book').click()
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(int(x)))

browser.find_element(By.CSS_SELECTOR, '#answer').click()

time.sleep(10)
