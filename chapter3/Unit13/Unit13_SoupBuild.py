from bs4 import BeautifulSoup
from urllib.request import urlopen

# 使用字符串构建soup
soup1 = BeautifulSoup("<HTML><HEAD> 《headers》</HEAD> 《body》</HTML>")

# 使用本地文件构建soup
soup2 = BeautifulSoup(open("data/myDoc.html"))

# 使用Web文档构建soup
# 记住urlopen()不会添加"http://"
soup3 = BeautifulSoup(urlopen("http://hanwen.me/"))

# get_text() 返回标记文档中去除了所有标签的文本部分
result = soup2.get_text()
