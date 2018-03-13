#!/usr/bin python
# -*- coding:UTF-8 -*-
'''
#例子1
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j) and (i!=k) and (j!=k):
				print i,j,k
'''	
'''			
l=int(raw_input('li run:'))
arr=[1000000,600000,400000,200000,100000,0]
rate=[0.01,0.015,0.03,0.05,0.075,0.1]
bonus=0
for r in range(0,6):
	if l>arr[r]:
		bonus+=(l-arr[r])*rate[r]
		print('ti cheng:',(l-arr[r]*rate[r]))

l=arr[r]
print l
bonus=l+bonus
print bonus
'''
'''
#开头不懂
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

x = int(raw_input("净利润："))

if x<=100000:
    bonus=x*0.1
    print u"奖金:",bonus,u"元"
elif 100001<x<=200000:
    bonus=10000+(x-100000)*0.075
    print u"奖金:",bonus,u"元"
elif 200001<x<=400000:
    bonus=10000+7500+(x-200000)*0.05
    print u"奖金:",bonus,u"元"
elif 400001<x<=600000:
    bonus=10000+7500+10000+(x-400000)*0.03
    print u"奖金:",bonus,u"元"
elif 600001<x<=1000000:
    bonus=10000+7500+10000+6000+(x-600000)*0.015
    print u"奖金:",bonus,u"元"
elif 600001<x<=1000000:
    bonus=10000+7500+10000+6000+6000+(x-600000)*0.01
    print u"奖金:",bonus,u"元"
'''