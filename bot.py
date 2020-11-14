import time
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import LINK, THREADS, VIEWS, VIEW_DURATION


def start_thread_pool(threads=1):
    with ThreadPoolExecutor(max_workers=threads) as e:
        e.submit(start_bot)


def create_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    return webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)


def start_bot():
    driver = create_chrome_driver()
    driver.get(LINK)
    for i in range(VIEWS):
        time.sleep(VIEW_DURATION)
        driver.refresh()


if __name__ == "__main__":
    start_thread_pool(THREADS)