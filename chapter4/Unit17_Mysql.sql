# 在shell命令行启动mysql
mysql -u root -p

# 创建新的数据库用户和密码
CREAT USER 'duser'@'localhost' IDENTIFIED BY 'badpassw0rd';

# 给项目创建一个新的数据库（‘dsdb’）
CREAT DATABASE dsdb;

# 授予新用户对数据库的访问权限
GRANT ALL ON dsdb.* TO 'duser'@'localhost';

# 以用户的角色进入数据库
mysql -u duser -p dsdb

# 创建employee表
CREAT TABLE employee (empname TINYTEXT, salary FLOAT, hired DATE);

# 删除表
DROP TABLE employee;

CREATE TABLE employee (id INT PRIMARY KEY AUTO_INCREMENT,
					 updated TIMESTAMP, 
					 empname TINYTEXT NOT NULL,
					 salary FLOAT NOT NULL,
					 hired DATE);

# 给列加索引
ALTER TABLE employee ADD INDEX(hired);

# 删除索引
DROP INDEX hired ON employee;

# 唯一性约束, 若要添加的那一列是可变长度，则要指定长度
ALTER TABLE employee ADD UNIQUE(empname(255))