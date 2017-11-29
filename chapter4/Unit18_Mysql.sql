# 插入数据
INSERT INTO employee VALUES(NULL, NULL, "John Smith", 35000, NOW());

# 查询警告
SHOW WARNINGS;

# 在唯一性约束情况下，如果插入相同的数据，操作会被中止，如果加上关键字IGNORE，可以执行成功
INSERT INTO employee VALUES(NULL, NULL, "John Smith", 35000, NOW());	#插入失败，违反约束
INSERT IGNORE INTO employee VALUES(NULL, NULL, "John Smith", 35000, NOW()); # 插入成功，但是会有一条警告

# 删除操作
# 如果 John Smith 是一个低收入者，就将他的记录删除
DELETE FROM employee WHERE salary<11000 AND empname="John Smith";

# 删除所有记录
DELETE FROM employee;

# 删除特定记录,指定具体的条件
DELETE FROM employee WHERE id = 387513;

# 变更 or 更新
# 更新指定列的值，如果没有指定，则更新所有的记录

# 重置最新招入的员工工资
UPDATE employee SET salary=35000 WHERE hired=CURDATE();

# 再次增加John Smith 的工资
UPDATE employee SET salary=salary+1000 WHERE empname="John Smith";

# 选择 or 查询
SELECT empname, salary FROM employee WHERE empname='John Smith';

# 查询出的数据进行排序
SELECT * FROM employee WHERE hired>='2000-01-01' ORDER BY salary DESC;

# 查询招入日期在2001-01-01之后的，并求出其平均工资
SELECT (hired>'2001-01-01') AS Recent, AVG(salary) FROM employee GROUP BY (hired>'2001-01-01');

# 使用having对结果进行过滤
SELECT AVG(salary), MIN(hired), MAX(hired) FROM employee GROUP BY YEAR(hired) HAVING MIN(hired)>'2001-01-01';

# 连接操作
# 准备并填充另一张表
CREATE TABLE position (eid INT, description TEXT);
INSERT INTO position (eid, description) VALUES (6, 'Imposter'), (1, 'Accountant'), (4, 'Programmer'), (5, 'President');
ALTER TABLE position ADD INDEX(eid);

# 获取链接后的数据
SELECT employee.empname, position.description FROM employee, position WHERE employee.id=position.eid ORDER BY position.description;




