import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = ('https://jqueryui.com')
driver.get(url)
driver.maximize_window()
time.sleep(2)
all_links = driver.find_elements(By.TAG_NAME, "a")
print("the number of links is", {len(all_links)})
