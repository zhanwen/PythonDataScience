import urllib.parse

# print
# ParseResult(scheme='http', netloc='hanwen.me', path='', params='', query='', fragment='')
URL = "http://hanwen.me/2017/12/01/lucene-note/"
s = urllib.parse.urlparse(URL)
print(s)