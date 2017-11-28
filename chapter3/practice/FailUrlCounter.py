import urllib
from collections import Counter
import sys
from bs4 import BeautifulSoup

# use local file build soup
soup = BeautifulSoup(open("../data/myDoc.html"))
links = [(link.string, link['href']) for link in soup.find_all("a") if link.has_attr("href")]

# User dict save result
# key: url name, value: url
result = dict()

for link in links:
    url = link.get("href")
    try:
        with urllib.request.urlopen(url) as doc:
            print()
    except:
        result[link.string] = url

print(result)



