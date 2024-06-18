# https://github.com/mbnq/

import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to the chromedriver chromedriver.exe
# get it here https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.61/win64/chromedriver-win64.zip
chromedriver_path = r'C:\chromedriver\chromedriver.exe'

# URL
url = "https://www.mbnq.pl"

folder_path = "downloaded_images"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(30)

images = driver.find_elements(By.TAG_NAME, 'img')

for img in images:
    src = img.get_attribute('src')
    if src:
        filename = src.split('/')[-1]
        file_path = os.path.join(folder_path, filename)
        response = requests.get(src)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {file_path}")

driver.quit()
