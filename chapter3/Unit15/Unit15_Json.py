import json

object = "{student:[" \
             "{'name':'zhangsan', age:12}," \
             "{'name':'lisi', age:23}]" \
         "}"

# 将对象保存到文件
with open("/Users/zhanghanwen/Coding/Github/PythonDataScience/chapter3/data/data.json", "w") as out_json:
    json.dump(object, out_json, indent=None, sort_keys=False)


# 从文件载入对象
with open("/Users/zhanghanwen/Coding/Github/PythonDataScience/chapter3/data/data.json") as in_json:
    object1 = json.load(in_json)

# 将对象序列化为字符串
json_string = json.dumps(object1)


# 将字符串解析为json
object2 = json.loads(json_string)

