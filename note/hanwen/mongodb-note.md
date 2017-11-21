---
title: mongodb数据库学习
date: 2017-11-11 21:53:54
tags:
	- MongoDB
	- 数据库
---
关系型数据库
	
	Mysql、SqlServer、Oracle
	
非关系型数据库(Nosql not only sql)
	
	Redis、MongoDB、HBase、BigTable、CouchDB、Neo4j

结构化的数据：固定的长度、固定的类型、固定的格式。非结构化的数据：avi，ppt，doc

非关系型数据库的优点：
	
	1. 简单的扩展
	2. 快速的读写
	3. 低廉的成本
	4. 灵活的数据模型

非关系型数据库的不足之处：

	1. 不提供对SQL的支持
	2. 支持的特性不够丰富
	3. 现有的产品不够成熟

<!-- more -->

MongoDB是用C++语言编写的非关系型数据库。特点是高性能、易部署、易使用，存储数据十分方便，主要特性有：
```	
	面向集合存储，易于存储对象类型的数据
	模式自由
	支持动态查询
	支持完全索引，包含内部对象
	支持复制和故障恢复
	使用高效的二进制数据存储，包括大型对象
	文件存储格式为BSON(一种JSON的扩展)
```
MongoDB几本概念介绍
```	
	文档(document)是MongoDB中数据的基本单元，非常类似于关系型数据库系统中的行(但是比行要复杂的多)
	集合(collection)就是一组文档，如果说MongoDB中的文档类似于关系型数据库中的行，那么集合就如同表
	MongoDB的单个计算机可以容纳多个独立的数据库，每一个数据库都有自己的集合和权限
	MongoDB自带简洁但功能强大的JavaScript shell，这个工具对于管理MongoDB实例和操作数据作用非常大
	每一个文档都有一个特殊的键"_id",它在文档所处的集合中是唯一的，相当于关系数据库中的表的主键
```

MongoDB数据类型

| 数据类型  | 描述	| 举例		|
| ------------- | ------------- |
| null 	     |  表示空值或者未定义的对象 	                   |    {"x":null}
| 布尔值 	 |      真或者假：true或者false 	               |        {"x":true}
| 32位整数    |       32位整数。								| shell是不支持该类型的，shell中默认会转换成64位浮点数 	 
| 64位整数    |       64位整数。								| shell是不支持该类型的，shell中默认会转换成64位浮点数 	 
| 64位浮点数  |     64位浮点数。								| shell中的数字就是这一种类型 	      {"x"：3.14，"y"：3}
| 字符串 	 |      UTF-8字符串 	                           |    {"foo":"bar"}
| 符号 	     |  											| shell不支持，shell会将数据库中的符号类型的数据自动转换成字符串 	 
| 对象id 	 |      文档的12字节的唯一id 	                   |    {"id": ObjectId()}
| 日期 	     |  从标准纪元开始的毫秒数 	                   |    {"date":new Date()}
| 正则表达式   | 文档中可以包含正则表达式，遵循JavaScript的语法  |  {"foo":/foobar/i}
| 代码 	     |  文档中可以包含JavaScript代码 	              	| {"x"：function() {}}	 
| 未定义 	 |      undefined 	                           |    {"x"：undefined}
| 数组 	     |  值的集合或者列表 	                           |    {"arr": ["a","b"]}
| 内嵌文档    |       文档可以作为文档中某个key的value 	       |        {"x":{"foo":"bar"}}

为何要用非关系型数据库
&emsp;&emsp;在关系型数据库当中为某一个记录扩展一个字段方便吗？不方便，必须要改表结构.在非关系型数据库中，它的结构不固定，每条记录可以有不一样的键，每条记录可以根据需要增加一些自己的键值对

mongodb的安装

	将mongodb根目录下bin的路径加到环境变量中即可。

启动mongodb

	1. 新建一个mongodb的数据存放路径
	2. mongodb --dbpath=存放路径 (=号两边不要有空格)

默认占用一个端口对外提供服务（默认端口27017）

客户端连接，默认情况连接是不需要认证的，直接在命令行或者终端中输入下面命令，就可以连接到mongodb的服务器端
	
	mongo ip:port
	
新建数据库和删除数据库

	use xxx	//新建数据库
	db.dropDatabase() 	//删除当前数据库

查看所有数据库和查看当前数据库
	
	show dbs    //查看所有数据库
	db 			//当前数据库

查看当前数据库中所有的集合

	show collections or show tables

新建集合的两种方式，第一种隐式创建
	
	//在创建集合的同时往集合里面添加数据
	db.c1.insert({name:"zhangsan", age:1});

第二种显示创建
	
	db.createCollection(); 

向集合中插入数据
	
	db.collectionName.insert({key:value, key:value})
	
删除集合中的文档

	db.collectionName.remove({删除条件})	//若不加删除条件为删除集合中的所有文档

查询集合中的文档
	
	db.collectionName.find({查询条件})
	db.collectionName.findOne()
	//查询集合中的文档，返回某些特定的键值，0表示返回不包含该key的所有列，若是1表示返回该key字段
	db.collectionName.find({查询条件}, {key:0})	
	//注：_id字段始终都会被返回，哪怕没有明确指定

查询集合中的文档，使用条件表达式(<, <=, >, >=, !=)

	//大于： field > value
	db.collection.find({field:{$gt:value}});

	//小于： field < value
	db.collection.find({field:{$lt:value}});

	//大于等于： field >= value
	db.collection.find({field:{$gte:value}});

	//小于等于： field <= value
	db.collection.find({field:{$lte:value}});

	//不等于：  field != value
	db.collection.find({field:{$ne:value}});

查询集合中的文档，统计(count)、排序(sort)、分页(skip, limit)

	db.collectionName.count();
	db.collectionName.find().count();
	db.collectionName.find({age:{$lt:5}}).count();
	db.collectionName.find().sort({age:1}); 降序-1
	db.collectionName.find().skip(2).limit(3);
	db.collectionName.find().sort({age:-1}).skip(2).limit(3);
	db.collectionName.find().sort({age:-1}).skip(2).limit(3).count();
	db.collectionName.find().sort({age:-1}).skip(2).limit(3).count(0);
	db.collectionName.find().sort({age:-1}).skip(2).limit(3).count(1);

查询集合中的文档 ,$all主要用来查询数组中的包含关系，查询条件中只要有一个不包含就不返回
	
查询集合中的文档 ,$in，类似于关系型数据库中的IN

查询集合中的文档 ,$nin，与$in相反

查询集合中的文档 ,$or，相当于关系型数据库中的OR，表示或者的关系，例如查询name为user2或者age为3的文档，命令为：

	db.collectionName.find({$or:[{name:”user2”},{age:3}]})

查询集合中的文档 ,$nor，表示根据条件过滤掉某些数据，例如查询name不是user2，age不是3的文档，命令为：
	
	db.collectionName.find({$nor:[{name:”user2”},{age:3}]})

查询集合中的文档 ,$exists，用于查询集合中存在某个键的文档或不存在某个键的文档，例如查询customer集合中存在name键的所有文档，可以使用 

	//$exists:1表示真，指存在
	//$exists:0表示假，指不存在
	db.customer.find({name:{$exists:1}})，

更新集合中的文档

	//criteria:用于设置查询条件的对象
	//objNew:用于设置更新内容的对象
	//upsert:如果记录已经存在，更新它，否则新增一个记录，取值为0或1
	//multi：如果有多个符合条件的记录，是否全部更新，取值为0或1
	db.collection.update(criteria, objNew, upsert, multi)

注意：默认情况下，只会更新第一个符合条件的记录一般情况下后两个参数分别为0,1 ，即：
	
	db.collection.update(criteria,objNew,0,1)

更新集合中的文档, $set 用来指定一个键的值，如果这个键不存在，则创建它。例如：给name为user1的文档添加address，可以使用命令：
	
	db.c1.update({name:”user1”},{$set:{address:”bj”}},0,1)

将name为user1的文档修改address为tj，其它键值对不变,命令为：
	
	db.c1.update({name:”user1”},{$set:{address:”tj”}},0,1)

更新集合中的文档,使用 $inc 将集合中name为user1的age加1，其它键不变, $inc表示使某个键值加减指定的数值

	db.c1.update({name:”user1”},{$inc:{age:1}})

更新集合中的文档, $unset 用来删除某个键，例如删除name为user1的文档中的address键，可以使用命令：
	
	db.collectionName.update({name:”user1”},{$unset:{address:1}},0,1)

索引就是用来加速查询的。数据库索引与书籍的索引类似：有了索引就不需要翻遍整本书，数据库则可以直接在索引中查找，使得查找速度能提高几个数量级。在索引中找到条目以后，就可以直接跳转到目标文档的位置。

	//创建普通索引
	db.collection.ensureIndex({key:1})
	//查看关于索引的相关信息
	db.collection.stats()
	//查看查询使用索引的情况
	db.collection.find({key:value}).explain()
	//删除索引
	db.collection.dropIndex({key:1})
	//删除集合，也会将集合中的索引全部删除

	//创建唯一索引
	db.collection.ensureIndex({key:1}，{unique:true})
	//查看关于索引的相关信息
	db.collection.stats()
	//查看查询使用索引的情况
	db.collection.find({key:value}).explain()
	//删除索引
	db.collection.dropIndex({key:1})
	//删除集合，也会将集合中的索引全部删除

固定集合指的是事先创建而且大小固定的集合。固定集合特性：固定集合很像环形队列，如果空间不足，最早的文档就会被删除，为新的文档腾出空间。一般来说，固定集合适用于任何想要自动淘汰过期属性的场景，没有太多的操作限制。创建固定集合使用命令
	
	//size指定集合大小，单位为KB，max指定文档的数量 
	db.createCollection(“collectionName”,{capped:true,size:100000,max:100});  

当指定文档数量上限时，必须同时指定大小。淘汰机制只有在容量还没有满时才会依据文档数量来工作。要是容量满了，淘汰机制会依据容量来工作。 


备份(mongodump)和恢复(mongorestore)
MongoDB提供了备份和恢复的功能，分别是MongoDB下载目录下的mongodump.exe和mongorestore.exe文件,备份数据使用下面的命令：
	
	//-h：MongDB所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017
    //-d：需要备份的数据库实例，例如：test
    //-o：备份的数据存放位置，例如：c:\data\dump，当然该目录需要提前建立，在备份完成后，系统自动在dump目录下建立一个test目录，这个目录里面存放该数据库实例的备份数据。
	mongodump -h dbhost -d dbname -o dbdirectory

恢复数据使用下面的命令：
	
	//-h：MongoDB所在服务器地址
    //-d：需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2
    //-directoryperdb：备份数据所在位置，例如：c:\data\dump\test
	mongorestore -h dbhost -d dbname -directoryperdb dbdirectory

导入(mongoimport)和导出(mongoexport)
导出数据可以使用命令

    //-h 数据库地址
    //-d 指明使用的库
    //-c 指明要导出的集合
    //-o 指明要导出的文件名
	mongoexport -h dbhost -d dbname -c collectionName -o output

导入数据可以使用命令：
	
	//-h 数据库地址
    //-d 指明使用的库
    //-c 指明要导入的集合
	mongoimport -h dbhost -d dbname -c collectionname 文件的地址...

安全和认证
每个MongoDB实例中的数据库都可以有许多用户。如果开启了安全性检查，则只有数据库认证用户才能执行读或者写操作。在认证的上下文中，MongoDB会将普通的数据作为admin数据库处理。admin数据库中的用户被视为超级用户(即管理员)。在认证之后，管理员可以读写所有数据库，执行特定的管理命令，如listDatabases和shutdown。在开启安全检查之前，一定要至少有一个管理员账号。

在admin数据库中创建管理员账号：
	
	use admin;
	db.addUser(“root”,”root”);

在test数据库中创建普通账号：
	
	use test;
	db.addUser(“zhangsan”,”123”);
	db.addUser(“lisi”,”123”,true);

注意：用户zhangsan，密码为123，对test数据库拥有读写权限，用户lisi，密码为123，对test数据库拥有只读权限

重新启动数据库服务，并开启安全检查
	
	mongod --dbpath d:\mongo_data --auth







