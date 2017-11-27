from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen("http://hanwen.me") as doc:
    soup = BeautifulSoup(doc)

    links = [(link.string, link['href'])
                for link in soup.find_all("a")
                    if link.has_attr("href")]
