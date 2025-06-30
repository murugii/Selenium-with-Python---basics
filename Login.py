import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#test the herokuapp with the url: https://the-internet.herokuapp.com/login
url = "https://the-internet.herokuapp.com/login"
#declare the username and password variables
username = "tomsmith"
password = "SuperSecretPassword!"

driver.get(url)
driver.maximize_window()
time.sleep(4)
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

#pass the username and passwords
username_field.send_keys(username)
password_field.send_keys(password)

#find and click the login button
driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()

# verify that the login was successful by, e.g, confirming that the "Secure Area" text on the landing page is visible
login_success = driver.find_element(By.XPATH, "//h2[normalize-space()='Secure Area']")
assert login_success.text == "Secure Area"
time.sleep(3)

# find and click the logout button
driver.find_element(By.XPATH, "//i[@class='icon-2x icon-signout']").click()
time.sleep(4)
