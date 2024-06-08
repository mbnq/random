import requests
from bs4 import BeautifulSoup
import os

# URL
url = "https://www.mbnq.pl/"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html5lib')
folder_name = "output_data"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open(os.path.join(folder_name, "content_html.txt"), "wb") as file:
    file.write(content)

text = soup.get_text()
with open(os.path.join(folder_name, "content_text.txt"), "w", encoding='utf-8') as file:
    file.write(text)

links = soup.find_all('a')
urls = [link.get('href') for link in links if link.get('href')]
with open(os.path.join(folder_name, "content_links.txt"), "w", encoding='utf-8') as file:
    for url in urls:
        file.write(f"{url}\n")

images = soup.find_all('img')
image_urls = [img.get('src') for img in images if img.get('src')]
with open(os.path.join(folder_name, "content_images.txt"), "w", encoding='utf-8') as file:
    for img_url in image_urls:
        file.write(f"{img_url}\n")

for i, img_url in enumerate(image_urls):
    img_data = requests.get(img_url).content
    img_name = f"image_{i+1}.jpg"
    with open(os.path.join(folder_name, img_name), 'wb') as img_file:
        img_file.write(img_data)

print(f"Done. Grab it here {folder_name}")
