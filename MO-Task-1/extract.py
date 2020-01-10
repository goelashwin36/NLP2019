# This script was used to fetch links from the source URL.

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests

resp = requests.get("https://hindi.speakingtree.in/blog-list")
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, from_encoding=encoding)

for link in soup.find_all('a', href=True):
    print(link['href'])
