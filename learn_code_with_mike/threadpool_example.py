from bs4 import BeautifulSoup
import requests
import time
import concurrent.futures

def scrape(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "lxml")

    titles = soup.find_all("h3", {"class": "post_title"})

    for title in titles:
        print(title.getText().strip())

    time.sleep(2)


base_url = "https://www.inside.com.tw/tag/AI"

urls = [f"{base_url}?page={page}" for page in range(1, 6)]

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scrape, urls)

end_time = time.time()

print(f"{end_time - start_time} PARSED {len(urls)} PAGES OF POSTS")

