#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
list=['abc','jack','Taobao']
list_pop1=list.pop(0)
list_pop2=list.pop(1)
print "第一次删除的项为:",list_pop1
print "第二次删除的项为:",list_pop2
print "列表现在为:",list
'''
'''
count=0
while(count<9):
    print 'The count is:',count
    count+=1
print "Good bye!"
'''
'''
i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i
i=1
while 1:
    print i
    i+=1
    if(i>10):
        break
'''
'''
#无限循环
var=1
while var==1:
    num=raw_input("输入一个数：")
    print "你输入的数为：",num
'''
'''
count=0
while count<5:
    print count,"is less than 5"
    count+=1
else:
    print count,"is not less than 5"
'''
'''
#九九乘法表
i = 1
while i:
    j = 1
    while j:
        print j, "*", i, " = ", i * j, '  ',
        if i == j:
            break

        j += 1
        if j >= 10:
            break

    print "\n"  
    i += 1
    if i >= 10:
        break
'''
'''
print('1024*768=',1024*768)
print '1024*768=',1024*768
print('100 + 200 =', 100 + 200)
print('I\'m OK')
'''
'''
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
else:
    print(0)
#输出逻辑：首先i=0<5,则不会执行else

x=12
def f1():
    x=3
    print(x)
def f2():
    x+=1
    print(x)
f1()
f2()
'''
#print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))
'''
a1=72
a2=85
p=(a2-a1)*100/a1
print('小明成绩提高的百分点：%.1f %%' % p)
print('小明的成绩提高百分点{0:.1f}%'.format(p))
'''
'''
#输出N以内的素数
import math
l = []
n = int(input('please input a number more than 2:'))
if n == 2:
    print('there is no prime less than 2!')
else:
    for a in range(2, n):
        for b in range(2, int(math.sqrt(a)) + 1):#素数只需要不能整除2-根号自己就可以了。
            l.append(a % b)#将所有b遍历的结果加到列表中
        if 0 not in l:
            print(a)
        l = []
'''
'''
#计算两个数之和
#写法一：
num1=input('输入第一个数字：')
num2=input('输入第二个数字：')
sum=float(num1)+float(num2)    #input返回一个字符串，用float()方法将字符串转换为数字
print('数字{0}和{1}相加结果为：{2}'.format(num1,num2,(sum)))

#一行代码输出:
print('两个数之和为%0.1f' % (float(input('输入第一个数：'))+float(input('输入第二个数：'))))
'''
