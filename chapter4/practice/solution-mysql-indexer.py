import nltk, pymysql

infilename = input("Enter the name of the file to index: ")

# 结合你的MySQL服务器的设置改变本行
conn = pymysql.connect(user="duser", passwd="badpassw0rd", db="dsdb")
cur = conn.cursor()

QUERY = "INSERT INTO indexer (word, position, pos) VALUES "
wpt = nltk.WordPunctTokenizer()

offset = 1

with open(infilename) as infile:
    # 使用增量方式处理文本，每次处理一行
    # 无论如何，一个词不可能跨行分布
    for text in infile:
        # 分词并加入POS标签
        pieces = enumerate(nltk.pos_tag(wpt.tokenize(text)))

        # 创建一个查询命令，别忘了要避开待查询的词
        words = ["(\"%s\", %d, \"%s\")" % (conn.escape_string(w), i+offset, conn.escape_string(pos)) for (i, (w, pos)) in pieces]

        # 执行查询命令
        if words:
            cur.execute(QUERY + ','.join(words))

            # 移动词的位置指针
            offset += len(words)
conn.commit()
conn.close()