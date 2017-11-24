# open file demo
# mode="r" r(readyonly)
f = open("data.txt", mode="r")
s = f.read()
# print(s)
f.close()

# another way
# not need manual close file
with open("data.txt") as f:
    text = f.read()
    # print(text)

# read n byte
f = open("data.txt", mode="r")
s = f.read(10)
# print(s)
f.close()

# read next one line
f = open("data.txt", mode="r")
s = f.readline()
# print(s)
f.close()

# read full
f = open("data.txt", mode="r")
s = f.readlines()
# print(s)
f.close()

with open("data.txt", mode="w+b") as f:
    line = b"new context "
    f.write(line)
