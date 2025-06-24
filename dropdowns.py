import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = 'https://the-internet.herokuapp.com/dropdown'
driver.get(login_url)
time.sleep(3)
dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)

#select.select_by_visible_text("Option 2")
#time.sleep(2)
#select the value by visible text
#select the value by index
#select the option by using a value
target_value = "Option 2"
#select.select_by_visible_text("Option 2")
#select.select_by_index(1)
#select.select_by_value("1")
for option in select.options:
 if option.text == target_value:
      option.click()
      print(f"you have selected {target_value}")
      break
 else:
      print(f"you have not slected {target_value}")







