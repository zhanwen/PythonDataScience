import urllib.request, urllib.parse
import bs4 as BeautifulSoup

# 建立与用户以及网络的会话
base = input("Enter the URL: ")
try:
    page = urllib.request.urlopen(base)
except:
    print("Cannot open %s" % base)
    quit()

# 准备soup
soup = BeautifulSoup.BeautifulSoup(page)

# 提取链接，并用（名称，网址）的元组表示
links = [(link.string, link['href']) for link in soup.find_all("a") if link.has_attr("href")]

# 尝试打开每个链接
broken = False

for name, url in links:
    # 将base和链接目标组合在一起，因为页面内的链接都是相对地址，所以这里要与base结合在一起
    # 例如： base=http://hanwen.me     url=/about
    # dest = http://hanwen.me/about
    dest = urllib.parse.urljoin(base, url)
    print(dest)
    try:
        page = urllib.request.urlopen(dest)
        page.close()
    except:
        print("Link \"%s\" to \"%s\" is probably broken." %(name, dest))
        broken = True
# 显示好消息
if not broken:
    print("Page %s does not seem to have broken links. " %base)