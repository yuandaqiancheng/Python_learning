#!/usr/bin/env python
# -*- coding:UTF-8 -*-
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

#写法二：一行代码输出
print('两个数之和为%0.1f' % (float(input('输入第一个数：'))+float(input('输入第二个数：'))))
'''
'''
#计算平方根
#计算一个正数的平方根：写出该数的0.5次方即可
num=float(input('输入一个正数：'))
num_sqrt=num**0.5
print(('%0.3f的平方根为%0.3f')%(num,num_sqrt))

#计算负数和复数平方根：
import cmath   #导入复数数学模块
num=int(input('输入一个数字：'))
num_sqrt=cmath.sqrt(num)
print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))   #注意format中分隔只能用逗号


#两者综合，判断所有数
#注意0既不是正数也不是负数
import cmath
num=float(input('输入一个数：'))
if(num==0):
    print(0)
elif(num>0):
    num_sqrt=num**0.5
    print('%0.1f的平方根为%0.1f'%(num,num_sqrt))
else:
    num_sqrt=cmath.sqrt(num)
    print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))
'''
'''
#计算二次方程ax**2+bx+c=0的根,其中a,b,c由用户提供
#可能会有复数，导入cmath模块
import cmath
a=float(input('输入a:'))
b=float(input('输入b:'))
c=float(input('输入c:'))
d=b**2-4*a*c
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('结果为{0}，{0}'.format(sol1,sol2))

#优化一下，考虑到无穷解和的情况
import cmath
#a,b,c=input('依次输入三个数(空格分隔)：').split()     #这句不知道为啥有错误
a=float(input('输入a:'))
b=float(input('输入b:'))
c=float(input('输入c:'))
d=b**2-4*a*c
if(a==0 and b==0 and c==0):
    print('有无穷多个解')
else:
    x1=(-b-cmath.sqrt(d))/(2**a)
    x2=(-b+cmath.sqrt(d))/(2**a)
    print('方程的解为{0}，{1}'.format(x1,x2))

#此处不用考虑判断d，因为都可以算出来，具体原因不详
#else:
#    d=4*a*c-b**2
#   x1=(-b-cmath.sqrt(d))/(2**a)
#   x2=(-b+cmath.sqrt(d))/(2**a)
#   print('方程的解为{0},{1}'.format(x1,x2))
'''
'''
#计算三角形的面积，用户输入三边长度
#公式：应用海伦公式 S=(p(p-a)(p-b)(p-c)）**0.5 ，其中p为半周长
a=float(input('输入第一个边长：'))
b=float(input('输入第二个边长：'))
c=float(input('输入第三个边长：'))
p=(a+b+c)/2   #计算半周长
s=(p*(p-a)*(p-b)*(p-c))**0.5
print('三角形的面积为%0.3f'%s)  #记住要格式化输出，不然中文输出可能乱码
#优化：增加一个判断三边是否构成三角形
a=float(input('输入第一个边长：'))
b=float(input('输入第二个边长：'))
c=float(input('输入第三个边长：'))
while(a+b<c or a+c<b or b+c<a):
    print('不能构成三角形，请重新输入：')
    a = float(input('输入第一个边长：'))
    b = float(input('输入第二个边长：'))
    c = float(input('输入第三个边长：'))
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print('三角形的面积为%0.3f'%s)
'''

a=set([1,2,3])
print(a)


