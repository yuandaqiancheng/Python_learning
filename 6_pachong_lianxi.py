#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#print([str(round(355/113,i)) for i in range(1,6)])   #输出有问题，没有按照小数点位数递增输出

#循环之一：for...in循环,依次把list或tuple中的每个元素迭代出来
names=['jack','john','tom']
for name in names:
    print(name)

#计算1-10的和
sum=0
list=[1,2,3,4,5,6,7,8,9,10]
for x in list:
    sum+=x
print(sum)
#计算1-100，用range()函数
sum=0
print(range(1,101))
for x in range(1,101):
    sum+=x
print(sum)
#循环之二：while循环
#计算100以内的奇数之和可以用while
sum=0
n=1
while(n<100):
    sum+=n
    n+=2
print(sum)
#
sum=0
n=99
while(n>0):
    sum+=n
    n-=2
print(sum)
#如果是单独新建一个.py的文件定义函数，再来调用的话写法如下
from abstest import my_abs #注意：这里的abstest是文件名不包含.py拓展名
print(my_abs(-9))

def power1(x):
    return (x**2)
print(power1(-2))

def power2(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s    #一定注意，最后返回一个值一定不要在循环里面写，简单说就是向前缩进
print(power2(5,3))
#默认参数:好处是能降低调用函数的难度
def power3(x,n=2):    #注意：这里的默认参数不能直接写2，否则报错
    s=1
    while(n>0):
        n=n-1
        s=s*x
    return s
print(power3(5))
print(power3(5,3))   #此时对于n > 2的其他情况，就必须明确地传入n，相当于n=3
#注意:设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数

#例如：写个一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
print(enroll('jack','F'))
#继续加入年龄和城市，我们可以把年龄和城市设为默认参数
def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
enroll('john','D')
#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
#因为list可变
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end(['a','b','c']))  #前两个调用是有给参数，就是对函数的正常调用
print(add_end())   #当没有参数调用时，第一次对的
print(add_end())   #在第一次调用后，接着不给参数调用即是使用默认的参数，因为list可变，Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了
print(add_end())   #同理，多次调用改变了L的内容
#注意：定义默认参数要求：默认参数必须指向不变对象！原因：因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误

#修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())   #无论调用多少次都不会有问题
#循环遍历的两种方式
f=['banana','apple','mango']
for i in f:   #方法一：直接for循环遍历
    print(i)
for i in range(len(f)):   #方法二：在for循环中加上range(),要注意输出写法
    #print(i)   #这个只是输出索引i
    print(f[i])  #如果要加上range()输出列表f的内容要写f[i]
###例子：给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
#由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc1(numbers):   #传参数时给number传一个列表或者元组
    sum=0
    for n in numbers:  #循环遍历numbers中的参数出来
        sum=sum+n*n
    return sum
print(calc1([1,3,5]))  #传参数：传一个列表
print(calc1((2,3,1)))  #传一个元组
#利用可变参数,则只要在定义时在参数前加*，在调用时就可以简化
def calc2(*numbers):  #定义函数时发现*就是可变参数
    sum=0
    for n in numbers:
        sum=sum+n**2
    return sum
print(calc2(1,3,5))  #调用时就更简单，直接写参数1,3,5
print(calc2(2,3,1))
print(calc2())   #输出0
#注意：以后写可变参数就写后者更简练
#如果已经有一个list或者tuple，要调用一个可变参数怎么办(就是给calc()函数的参数是list或者tuple)：
nums=[4,5,1]
b=calc2(*nums)  #在定义加*的基础上（就是利用了可变参数），给的参数为list或者tuple，在其名字前加*就会把list或tuple的元素变成可变参数传进去
print(b)
#小爬虫
import requests
from pyquery import PyQuery as pq

url = 'http://zhixing.bjtu.edu.cn/portal.php'
r = requests.get(url)
p = pq(r.text).find('#portal_block_617 li>a')
for d in p:
    print pq(d).text()
    print 'http://zhixing.bjtu.edu.cn/'+pq(d).attr('href')
#关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('jack',20)
