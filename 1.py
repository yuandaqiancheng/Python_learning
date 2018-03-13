#!/usr/bin/env python
# -*- coding:utf-8 -*-
#print "hello girl"

'''print "hello girl"
print "hello girl"
print "hello girl"'''

'''user = input("请输入用户名：")
pwd = input("请输入密码：")
print("用户名：%s,密码：%s"%(user,pwd))'''

'''str='Hello World'
print str
print str[0]
print str[2:7]
print str[2:]
print str*2
print str+"test"'''

'''list=['runoob',786,2.23,'john',70.2]
tinylist=[123,'john']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist*2
print list+tinylist'''
'''
list=["alex","oldboy","nosong","noway","nobody","jack"]
number=[1,2,3,4,5,6,7,8,9]
print("索引",list.index("nosong"))
print("切片",number[2:5])
print("步长",number[1:8:2])
number.append(10)
print("追加",number)
number.insert(3,444)
print("插入",number)
print("长度",len(number))
del number[0]
print("删除",number)
#循环输出值
for i in list:
	print(i) 
#带下标输出
for k,v in enumerate(list):
	print(k,v)
#包含
if "alex" in list:
	print("包含：yes")
'''
'''
tuple=('runoob',78,2.23,'john',70.2)
tinytuple=(123,'john')
print tuple
print tuple[0]
print tuple[1:3]	#输出第二个至第三个的元素
print tuple[2:]		#输出从第三个开始至列表末尾的元素
print tinytuple*2
print tuple+tinytuple
'''
'''
dict={}
dict['one']="This is one"   #键为one，value为等号右边的
dict[2]="This is two"		#同理
tinydict={'name':'john','code':6345,'dept':'sales'}
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
'''
'''
#访问元组
tup1=('physics','chemistry',1990,2001)
tup2=(1,2,3,4,5)

print "tup1[0]:",tup1[0]
print "tup2[1:4]:",tup2[1:4]

tup1=(12,23,34)
tup2=('abc','xyz')
#创建一个新的元组，进行连接组合
tup3=tup1+tup2
print tup3
'''
'''
#创建二维列表：list_2d = [[0 for col in range(cols)] for row in range(rows)]
list_2d=[[0 for i in range(5)]for i in range(6)]
print list_2d	
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(8)
print list_2d
'''
'''
#很多测试
tup=(1,2,3)
for i in tup:
    print i
tup=(2,3,4,5,6,7)
print len(tup)

L=('a','b','c','d')
print L[-2]     #反向读取，读取倒数第二个元素：c

print 'abc',-4.2e21,18+6j,'xyz'
x,y=1,2
print "Value of x,y:",x,y

print tuple([1,2,3,4])
print tuple({1:2,3:4})     #针对字典 会返回字典的key组成的tuple:(1,3)

dict={'Name':'john','Age':7,'Class':'First'}
print "dict['Name']:",dict['Name']
print "dict['Age']:",dict['Age']

#修改字典的方法是增加新的键/值对，修改或删除已有的键/值对
dict={'Name':'john','Age':7,'Class':'First'}
dict['Age']=8      #修改
print dict
dict['School']='Yi Ling School'  #增加
print dict
del dict['Name']   #删除键为'Name'的条目
print dict
dict.clear()       #清除dict字典的所有条目
print dict
del dict    	   #会引发一个异常，因为用del后字典不再存在	
print dict
'''
import getpass
name=input("input name:")
pwd=input("input password:")
#pwd=getpass.getpass("input name:")
if (name=='john') and (pwd=='123'):
	print("right!")
else:
	print("wrong!")
	