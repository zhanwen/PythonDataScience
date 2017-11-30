import pymongo as mongo

# 使用默认的初始化方式
# client1 = mongo.MongoClient()

# 指定主机和端口号
client2 = mongo.MongoClient("localhost", 27017)

# 使用URI方式指定主机和端口号
# client3 = mongo.MongoClient("mongodb://localhost:27017/")

# 创建并选择活动数据库的两种方法
db = client2.dsdb
# db = client1["dsdb"]

# 创建并选择活动集合的两种方法
people = db.people
# people = db["people"]

# person1 = {"empname": "John Smith", "dob":"1957-12-24"}
# person2 = {"_id": "XVT162", "empname":"Jane Doe", "dob":"1964-05-16"}
# person_id1 = people.insert_one(person1).inserted_id
# person_id2 = people.insert_one(person2).inserted_id
# print(person_id2)

persons = [{"empname":"Abe Lincoln", "dob":"1809-02-12"},
           {"empname":"Anon I. Muss"}]

# result = people.insert_many(persons)
# print(result.inserted_ids)

everyone = people.find()
# print(list(everyone))

oneResult = list(people.find({"dob":"1957-12-29"}))
# print(oneResult)

result = people.find_one()
# print(result)

# 根据empname查找
people.find_one({"empname":"Abe Lincoln"})

people.find_one({"_id":"XVT162"})

# list size
print(people.count())

count = people.find({"dob":"1957-12-24"}).count()
print(count)

people.find().sort("dob")

# delete operator
result = people.delete_many({"dob":"1957-12-24"})
print(result.deleted_count)