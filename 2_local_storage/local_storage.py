import os
from selenium import webdriver
from selenium.webdriver.common.by import By

file_path = os.path.abspath("local_storage.html")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(f"file://{file_path}")

driver.execute_script("localStorage.setItem('new-display', true);")
driver.refresh()

current_value = driver.find_element(By.ID, 'upload').text
expected_value = "Выбрать"
assert current_value == expected_value, f"Expected: {expected_value}, current: {current_value}"

driver.quit()
