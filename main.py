from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from concurrent.futures import ThreadPoolExecutor
from creds import *

# Function to launch browser in incognito mode (no cache)
def open_link_fresh(url, wait_time=10):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(wait_time)
    driver.quit()


# Open multiple browser sessions in parallel
with ThreadPoolExecutor(max_workers=repeat_count) as executor:
    futures = [
        executor.submit(open_link_fresh, url_to_open, 10)
        for _ in range(repeat_count)
    ]
    for i, f in enumerate(futures):
        f.result()  # Waits for completion
        print("Executed", i + 1)
