from bs4 import BeautifulSoup
from urllib.request import urlopen

# 使用字符串构建soup
soup1 = BeautifulSoup("<HTML><HEAD> 《headers》</HEAD> 《body》</HTML>")


