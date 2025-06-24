from time import sleep
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')
driver.maximize_window()
time.sleep(4)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.find_element(By.XPATH, "//div[@class='mt-40']//div//label[contains(text(),'Option 1')]//input[@type='checkbox']").click()
all_checkboxes = driver.find_elements(By.XPATH, 
time.sleep(5)