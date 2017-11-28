from nltk.tokenize import WordPunctTokenizer
import nltk
word_punct = WordPunctTokenizer()
text = "}Help! :))) :[ ...... :D{"
result = word_punct.tokenize(text)
# print(result)

result2 = nltk.word_tokenize(text)
# print(result2)

pstemmer = nltk.PorterStemmer()
stem = pstemmer.stem("wonderful")
# print(stem)

lstemmer = nltk.LancasterStemmer()
stems = lstemmer.stem("wonderful")
# print(stems)

lemmatizer = nltk.WordNetLemmatizer()
result = lemmatizer.lemmatize("wonderful")
# print(result)

pos_tag = nltk.pos_tag(["beautiful", "world", "a"])
# print(pos_tag)
