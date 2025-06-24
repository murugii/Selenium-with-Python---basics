from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
username = "tomsmith"
password = "SuperSecretPassword!"
login_url = "https://the-internet.herokuapp.com/login"
driver.get(login_url)
username_field = driver.find_element(By.ID, value="username")
password_field = driver.find_element(By.ID, value = "password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.CLASS_NAME, value = "radius")
assert not login_button.get_attribute("disabled")
login_button.click()

login_success = driver.find_element(By.CLASS_NAME, value = "flash")
assert "You logged into a secure area!" in login_success.text


