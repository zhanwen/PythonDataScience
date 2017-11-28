from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk import LancasterStemmer
import nltk

# 创建一个新词干
ls = nltk.LancasterStemmer()

# 读取文件并生成soup
with open("../data/index.html") as infile:
    soup = BeautifulSoup(infile)

# 提取并标记文本
words = nltk.word_tokenize(soup.text)

# 转换为小写
words = [w.lower() for w in words]

# 删除停用词，并分析剩余部分的词干
words = [ ls.stem(w) for w in words if w not in stopwords.words("english") and w.isalnum()]

# 对词进行计数
freqs = Counter(words)
print(freqs.most_common(10))