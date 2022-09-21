import os
from selenium import webdriver

file_path = os.path.abspath("pseudo_element.html")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(f"file://{file_path}")

current_value = driver.execute_script(
    "return window.getComputedStyle(document.querySelector(`.check`), ':before').getPropertyValue('background-image')")
expected_value = "11.Placeholder-512.png"
assert expected_value in current_value, f"Expected: {expected_value}, current: {current_value}"

current_value = driver.execute_script(
    "return window.getComputedStyle(document.querySelector(`.fail`), ':before').getPropertyValue('background-image')")
expected_value = "12.Placeholder-512.png"
assert expected_value in current_value, f"Expected: {expected_value}, current: {current_value}"

driver.quit()
