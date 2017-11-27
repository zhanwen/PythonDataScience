from bs4 import BeautifulSoup
from urllib.request import urlopen


# 使用本地文件构建soup
soup = BeautifulSoup(open("data/myDoc.html"))

# 返回标签<h2>的所有实例
level2headers = soup.find_all("h2")

# 返回粗体或斜体格式
formats = soup.find_all(["i", "b", "em", "strong"])

# 返回具有某个属性的所有标签
result = soup.find(id="link")

links = soup.find_all("a")
firstLink = links[0]["href"] # or links[0].get("href")
