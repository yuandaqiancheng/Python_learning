#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
num=5
if num==3:
	print 'boss'
elif num==2:
	print 'user'
elif num==1:
	print 'worker'
elif num<0:
	print 'error'
else:
	print 'roadman'
'''
'''
#if 语句多个条件
num=9
if num>=0 and num<=10:
	print 'hello'
num=10
if num<0 or num>10:
	print 'hello'
else:
	print 'undefine'
num=8
if (num>=0 and num<=5) or (num>=10 and num<=15):
	print 'hello'
else:
	print 'undefine'
'''


list=['abc','jack','Taobao']
list_pop1=list.pop(0)
list_pop2=list.pop(1)
print "第一次删除的项为:",list_pop1
print "第二次删除的项为:",list_pop2
print "列表现在为:",list