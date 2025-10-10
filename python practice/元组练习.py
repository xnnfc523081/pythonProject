# 元组基本操作
# 给定元组：numbers = (10, 20, 30, 40, 50, 60)
# 1. 访问第3个元素（索引为2）
# 2. 访问倒数第2个元素
# 3. 遍历元组并打印所有元素
# 4. 获取元组长度
# 5. 对元组进行切片，获取索引1到4（不包含4）的元素
from operator import index

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[2])
print(numbers[-2])
for i in numbers:
    print(i)
print(len(numbers))
print(numbers[1:4])

# 元组检查操作
# 给定元组：fruits = ("apple", "banana", "cherry", "orange", "grape")
# 1. 检查 "banana" 是否在元组中
# 2. 检查 "pear" 是否不在元组中
# 3. 查找 "orange" 的索引位置
# 4. 统计 "apple" 出现的次数
# 5. 查找 "cherry" 在索引1到4范围内的位置
fruits = ("apple", "banana", "cherry", "orange", "grape")
print("banana" in fruits)
print("pear" not in fruits)
print(fruits.index("orange"))
print(fruits.count("apple"))
print(fruits.index("cherry",1,4))

# 混合类型元素操作
# 给定混合类型元组：mixed = (1, "hello", 3.14, True, [1, 2, 3], {"name": "John"})
# 1. 访问字符串 "hello"
# 2. 访问列表 [1, 2, 3] 中的第二个元素
# 3. 检查数字 3.14 是否在元组中
# 4. 获取元组的长度
# 5. 查找布尔值 True 的索引位置
mixed = (2, "hello", 3.14, True, [1, 2, 3], {"name": "John"})
print(mixed[1])
print(mixed[4][1])
print(3.14 in mixed)
print(len(mixed))
print(mixed.index(True))

# 单元素元组和空元组
# 1. 创建一个只包含数字 5 的元组
# 2. 创建一个空元组
# 3. 检查数字 5 是否在第一个元组中
# 4. 检查第二个元组是否为空（长度为0）
# 5. 尝试修改单元素元组的第一个元素（观察会发生什么）
num = (5,)
num_1 = ()
print(5 in num)
print(len(num_1) == 0)
#num[0] = 1
#print(num)

# 元组的嵌套
# 给定嵌套元组：nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# 1. 访问第二个子元组 (4, 5, 6)
# 2. 访问数字 5（第二组第二列）
# 3. 遍历所有子元组并打印
# 4. 检查数字 8 是否在嵌套元组中
# 5. 统计数字 3 出现的次数
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested[1])
print(nested[1][1])
for i in nested:
    print(i)
for i in nested:
    if 8 in i:
        print(8 in i)
count = 0
for i in nested:
    if 3 in i:
        count += i.count(3)
print(count)


# 综合练习
# 给定元组：data = (1, 2, 2, 3, 4, 4, 4, 5)
# 1. 统计数字 2 出现的次数
# 2. 统计数字 4 出现的次数
# 3. 查找数字 3 的索引位置
# 4. 检查数字 6 是否不在元组中
# 5. 获取元组的长度
# 6. 对元组进行切片，获取前3个元素
# 7. 对元组进行切片，获取最后3个元素
data = (1, 2, 2, 3, 4, 4, 4, 5)
print(data.count(2))
print(data.count(4))
print(data.index(3))
print(6 not in data)
print(len(data))
print(data[0:3])
print(data[-3:])

# 元组与列表转换
# 1. 将列表 [1, 2, 3, 4, 5] 转换为元组
# 2. 将元组 ('a', 'b', 'c') 转换为列表
# 3. 检查转换后的元组中是否包含数字 3
# 4. 检查转换后的列表中是否包含字母 'b'
T = tuple([1,2,3,4,5])
print(T)
L = (list(('a','b','c')))
print(L)
print(3 in T)
print('b' in L)

