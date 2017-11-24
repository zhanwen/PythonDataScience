# list demo
from timeit import timeit
# 删除myList中的重复项
myList = [-1, 1, 2, 3]
myList = list(set(myList))

bigList = [str(i) for i in range(100000)]
"abc" in bigList   # 耗时0.2秒
bigSet = set(bigList)
"abc" in bigSet  # 耗时15-30微秒

# key:value
# key is default seq index and first index is zero, value is string
# print {0: 'alpha', 1: 'charlie', 2: 'bravo', 3: 'delta'}
seq = ["alpha", "charlie", "bravo", "delta"]
d = dict(enumerate(seq))

# key:value
# print {'a': 'alpha', 'b': 'charlie', 'c': 'bravo', 'd': 'delta'}
kseq = "abcd"
vseq = ["alpha", "charlie", "bravo", "delta"]
d = dict(zip(kseq, vseq))

# myList = [1, 2, 3, -1]
# copy myList
# print [1, 2, 3, -1]
l = [x for x in myList]

# print great than zero
# print [1, 2, 3]
l = [x for x in myList if x >= 0]

# element square in myList
# print [1, 4, 9, 1]
l = [x**2 for x in myList]

l = [1/x for x in myList if x != 0]

infile = "  hello world  "
s = [l.strip() for l in infile if l.strip()]
# or
[line for line in [l.strip() for l in infile] if line]

# () will generator object
# print <generator object <genexpr> at 0x101d927d8>
(x**2 for x in myList)
