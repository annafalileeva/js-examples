from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ckeditor.com/ckeditor-4/demo/#article")
driver.find_element(By.ID, 'document').click()
status = None
# while status != "ready":
#     status = driver.execute_script("return window.CKEDITOR.instances.ckdemo.status")
#     driver.execute_script(f"console.log('{status}')")
WebDriverWait(driver, timeout=10).until(
    lambda wd: wd.execute_script("return window.CKEDITOR.instances.ckdemo.status") == "ready", "No 'ready' status")
driver.quit()