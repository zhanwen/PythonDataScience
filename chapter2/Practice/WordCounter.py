import urllib.request
import sys
from collections import Counter
import re

# 建立与用户以及网络的绘画
url = input("Enter the url")
try:
    page = urllib.request.urlopen(url)

except:
    print("Could not open %s" % url)
    quit()

# 读取页面，并完成部分规范代码
doc = page.read().decode().lower()

# 将文本切分为词语
words = re.findall(r"\W+", doc)

# 构建计数器并给出结果
result = Counter(words)
print(result)