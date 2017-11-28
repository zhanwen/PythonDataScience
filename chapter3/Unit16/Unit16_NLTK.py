import nltk

# 语料库读取器
wn = nltk.corpus.wordnet
result = wn.synsets("cat")
# print(result)
# print(wn.synset("cat.n.01").definition())
# print(wn.synset("guy.n.01").definition())

# 同义词
cat = wn.synset("cat.n.01").hypernyms()
cat = wn.synset("cat.n.01").hyponyms()
# print(cat)

x = wn.synset("cat.n.01")
y = wn.synset("lynx.n.01")
rate = x.path_similarity(y)
# print(rate)

result = [simxy.definition() for simxy in max(
    (x.path_similarity(y), x, y)
    for x in wn.synsets('cat')
    for y in wn.synsets('dog')
    if x.path_similarity(y) # 确保synsets是相关的
)[1:]]

print(result)