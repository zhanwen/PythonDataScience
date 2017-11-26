import glob
import re
import os

dic = dict()
fileList = glob.glob("/Users/zhanghanwen/Coding/Github/PythonDataScience/chapter2/data/*.txt")

for file in fileList:
    path, filename = os.path.split(file)
    doc = open(file, mode="rb")
    result = doc.read().decode().lower()
    list = re.split(r"\W+", result)
    for word in list:
        if word not in dic:
            dic[word] = filename
        else:
            if filename in dic.get(word):
                continue
            else:
                value = [dic.get(word), filename]
                dic[word] = value

# print
# ['big.data.txt', 'public.policy.txt']
print(dic.get('txt'))

