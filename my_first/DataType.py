#数据类型
"""
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
"""
'''
#isinstance
a = 111
print(isinstance(a, int))
'''
"""
#运算
print(5 + 4)# 加法
print(4.3 - 2) # 减法
print(3 * 7) # 乘法
print(2 / 4) #除法，得到一个浮点数
print(2 // 4) # 除法，得到一个整数
print(17 % 3) # 取余
print(2 ** 5) # 乘方
"""
"""
#List（列表） 元素可改
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print(list)            # 输出完整列表
print(list[0])         # 输出列表第一个元素
print(list[1:3])       # 从第二个开始输出到第三个元素
print(list[2:])        # 输出从第三个元素开始的所有元素
print(tinylist * 2)    # 输出两次列表
print(list + tinylist) # 连接列表
"""
# Tuple（元组） 不可改

#Set（集合）  相当于数组;?
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

# Dictionary（字典） 无序的 键(key) : 值(value) 的集合。键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。 map