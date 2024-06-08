import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.mbnq.pl/"

response = requests.get(base_url)
if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, 'html5lib')
    links = soup.find_all('a')
    urls = [link.get('href') for link in links if link.get('href')]
    formatted_urls = []
    for url in urls:
        if url.startswith('/'):
            formatted_urls.append(base_url + url[1:])
        elif not url.startswith('http'):
            formatted_urls.append(base_url + url)
        else:
            formatted_urls.append(url)

    folder_name = "urloutput_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(os.path.join(folder_name, "output_all_links.txt"), "w", encoding='utf-8') as file:
        for url in formatted_urls:
            file.write(f"{url}\n")

    print("URLs gathered.")

else:
    print("Failed.")
