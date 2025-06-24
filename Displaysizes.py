import time
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


driver = webdriver.Chrome()
driver.get('https://google.com')
driver.maximize_window()
time.sleep(3)
display_sizes = [(281, 464),(400, 50),(412, 915),(430,932)]
try:
    for width,height in display_sizes:
        driver.set_window_size(width,height)
        time.sleep(3)
finally:
    driver.close()
