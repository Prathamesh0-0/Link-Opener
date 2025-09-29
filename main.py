from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import creds

# Function to launch browser in incognito mode (no cache)
def open_link_fresh(url, wait_time=5):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(wait_time)  # Wait for the page to load completely
    driver.quit()


for _ in range(repeat_count):
    open_link_fresh(url_to_open, wait_time=5)
    time.sleep(2)
    print("Executed ", _+1)
