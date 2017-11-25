import pickle

# 将一个对象转存dump到文件
s = "i love python"
with open("data/myData.pickle", "wb") as oFile:
    pickle.dump(s, oFile)


# 重新加载相同的对象
with open("data/myData.pickle", "rb") as iFile:
    object = pickle.load(iFile)
    print(object)