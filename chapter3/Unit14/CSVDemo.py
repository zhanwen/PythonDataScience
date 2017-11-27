import csv


with open("/Users/zhanghanwen/Coding/Github/PythonDataScience/chapter3/data/somefile.csv", newline='') as infile:
    reader = list(csv.reader(infile))
    data = list(reader)
    print(data)
    # 访问第一条记录
    idIndex = data[0]



