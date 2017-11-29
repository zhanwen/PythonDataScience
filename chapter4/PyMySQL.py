import pymysql

# 使用python连接mysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user="duser", password="badpassw0rd", db="dsdb")
cur = conn.cursor()

# 查询不需要提交
query = '''
    select employee.empname, position.description from employee, position where employee.id=position.eid
    order by position.description
    
'''
n_rows = cur.execute(query)
results = list(cur.fetchall())
# print(results)

# 新增之前记录数
select = "select * from employee"
count = cur.execute(select)
print(count)

# 新增一条记录
insert = "insert into employee values(NULL, NULL, 'Jik', 300000 ,NOW())"
cur.execute(insert)
conn.commit()

# 查询所有
count =  cur.execute(select)
print(count)