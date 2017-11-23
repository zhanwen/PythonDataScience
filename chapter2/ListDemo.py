# list demo
from timeit import timeit
# 删除myList中的重复项
myList = [1, 1, 2, 3]
myList = list(set(myList))
print(myList)


bigList = [str(i) for i in range(100000)]
print(bigList)

bigSet = set(bigList)
"abc" in bigSet