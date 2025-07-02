from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://selenium.dev"
driver.get(url)
driver.switch_to.new_window() #opens new tab
driver.get("https://playwright.dev") #loads this url on the second tab
print(f"You currently have {len(driver.window_handles)} browser tabs open") #find out how may tabs you have opened
current_tab = driver.current_window_handle
tab1 = driver.window_handles[0] #use indexing to identify your tabs
tab2 = driver.window_handles[1]
#use if statements to alternate between the tabs
if current_tab != tab1:
    driver.switch_to.window(tab1) 
driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()
