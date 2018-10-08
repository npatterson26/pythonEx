import requests
import re
from bs4 import BeautifulSoup


def main():
    spider(1, get_url())


def get_url():
    url = str(input("What webpage would you like to scrape? "))
    return url


def spider(max_pages, url):
    page = 1
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = link.get('href')
            print(href)


def download_file(url):
    r = requests.get(url, stream=True)
    open('google.ico', 'wb').write(r.content)


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    #return True
    """""
    Restrict by filesize
    """""
    content_length = header.get('content-length', None)
    if content_length and content_length > 2e8:  # 200 mb approx
        return False


main()
