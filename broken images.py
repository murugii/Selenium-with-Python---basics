import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://the-internet.herokuapp.com/broken_images"
driver.get(url)
time.sleep(2)
all_images = driver.find_elements(By.TAG_NAME, "img")
time.sleep(3)
print(f"Number of broken images:", {len(all_images)})

for image in all_images:
    src = image.get_attribute("src")
    natural_width = image.get_attribute("naturalWidth") #browser sets natural width to 0 if image is broken
    if natural_width == "0":
        print(f"broken image found {src}")

driver.quit()
