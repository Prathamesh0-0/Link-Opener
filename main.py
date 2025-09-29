from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from concurrent.futures import ThreadPoolExecutor


def open_link_fresh(url, wait_time=15):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(wait_time)
    driver.quit()

url_to_open = ("https://aiskillshouse.com/student/qr-mediator.html?uid=6592&promptId=17")
repeat_count = 10

for _ in range(repeat_count):
    with ThreadPoolExecutor(max_workers=repeat_count) as executor:
        futures = [
            executor.submit(open_link_fresh, url_to_open, 15)
            for _ in range(repeat_count)
        ]
        for i, f in enumerate(futures):
            f.result
            print("Executed", i + 1)
