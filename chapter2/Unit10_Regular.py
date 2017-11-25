import re

# 一个非字母数字字符进行划分
result = re.split(r"\W", "Hello, world!")
print(result)

# 合并所有相邻的非字母字符
result = re.split(r"\W+", "Hello, world!")
print(result)

mo = re.match(r"\d+", "067 Starts with a number")
print(mo.group())

mo2 = re.match(r"\d+", "Does not start with a number")
print(mo2)

# 不区分大小写
s = re.search(r"[a-z]+", "0010010 Has at least one 010 letter 0010010", re.I)
print(s.group())

# 区分大小写
s = re.search(r"[a-z]+", "0010010 Has at least one 010 letter 0010010")
print(s.group())

s = re.findall(r"[a-z]+", "0010010 Has at least one 010 letter 0010010", re.I)
print(s)

# print
# 0010010[...]010[...]0010010
s = re.sub(r"[a-z ]+", "[...]", "0010010 has at least one 010 letter 0010010")
print(s)

# print
# 0010010 repl repl repl repl 010 repl repl 0010010
s = re.sub(r"[a-z]+", "repl", "0010010 has at least one 010 letter and 0010010")
print(s)