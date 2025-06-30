import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://jqueryui.com/"
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME, "a")
time.sleep(5)
#find the total number of links in the entire page
print('total number of links is ',{len(all_links)})

#use the href attribute and a for loop to grab all the urls and find out if they are broken or not;any status greater than 400 should be considered broken
for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print("broken link", {href}, "status_code",{response.status_code})
driver.quit()
