# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
#a, b = 0, 1
#while b < 1000:
#    print(b,end=",")
#    a, b = b, a+b
"""
其中代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：
n=b
m=a+b
a=n
b=m
"""
