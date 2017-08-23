## -*- coding:utf-8 -*-  
from collections import Iterable
def fact(n):
	if n == 1:
		return 1;
	return fact(n-1)*n;

# a = fact(1000);
# print a;
# 尾递归优化
def fact1(n):
	return fact_iter(n, 1)
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num - 1,num*product)

# b = fact1(900)
# print b; 
L = ['a','b','c']
# 取前三个元素 或者[:3]
c = L[0:3] 
print c 
d = L[1:2];
print ['取1--2元素'] + d 
e = L[-2:]
print e ;
L1 = range(100)
print range(100)
# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for value  in d.itervalues():
	print value
# 列表生成器
print [x * x for x in range(1, 11) if x % 2 == 0]

L3 = ['Hello', 'World', 18, 'Apple', None] 
print [s.lower() for s in L3 if  isinstance(s,Iterable) ]

# 斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while max > n:
		yield b
		a,b = b,a+b
		n = n + 1
	# return b
'''
# 最难理解的就是generator和函数的执行流程不一样
# 。函数是顺序执行，遇到return语句或者最后一行函数
语句就返回。而变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
'''
print fib(10).next
# 高阶函数
def sumCC(x,y):
	return x+y
def gaojie(a , b , c):
	return c(a,b)
print gaojie(9, 10, sumCC)
