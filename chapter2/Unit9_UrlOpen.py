import urllib.request
import sys
try:
    with urllib.request.urlopen("http://www.networksciencelab.com") as doc:
        html = doc.read()
        print("Success!")
        # 如果数据读取成功，连接就会自动关闭
except:
    print("Could not open %s" % doc, file=sys.err)
    # 不要假装已经读到了文件！
    # 一定要在这里执行错误处理程序
    # file=sys.err 报语法错误，参见 issue2
