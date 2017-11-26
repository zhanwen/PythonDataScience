from collections import Counter

# list
phrase = "a man a plan a canal panama"
cntr = Counter(phrase.split())
s = cntr.most_common()
print(s)

# convert dict
s = cntrDict = dict(cntr.most_common())
print(s['a'])