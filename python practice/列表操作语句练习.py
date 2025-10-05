#  列表基本操作
# 给定列表：numbers = [10, 20, 30, 40, 50, 60]
# 1. 访问第3个元素（索引为2）
# 2. 访问倒数第2个元素
# 3. 遍历列表并打印所有元素
# 4. 获取列表长度
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[2])
print(numbers[-2])
for num in numbers:
    print(num)
print(len(numbers))  #这个没学过，多家练习



#  添加元素列表
# 给定空列表：fruits = []
# 1. 使用append添加 "apple"
# 2. 使用extend添加 ["banana", "cherry"]
# 3. 使用insert在索引1位置插入 "orange"
# 4. 在列表末尾添加数字 100
fruits = []
fruits.append("apple")
fruits.extend(["banana","cherry"])
print(fruits)
fruits.insert(1,"orange")
fruits.append(100)


#  修改与检查元素
# 给定列表：colors = ["red", "green", "blue", "yellow", "purple"]
# 1. 将索引2的元素改为 "pink"
# 2. 检查 "green" 是否在列表中
# 3. 检查 "black" 是否不在列表中
# 4. 查找 "yellow" 的索引位置
# 5. 统计 "red" 出现的次数
colors = ["red", "green", "blue", "yellow", "purple"]
colors[2] = "pink"
print("green" in colors)
print("black" not in colors)
print(colors.index("yellow"))
print(colors.count("red"))


#  删除元素练习
# 给定列表：data = [1, 2, 3, 4, 5, 6, 7, 8]
# 1. 使用del删除索引3的元素
# 2. 使用remove删除元素5
# 3. 删除最后一个元素
# 4. 删除前两个元素
data = [1, 2, 3, 4, 5, 6, 7, 8]
del data[3]
print(data)
data.remove(5)
print(data)
del data[0:2]  #这个没学过，需要多加练习
print(data)


#  排序和反转
# 给定列表：scores = [85, 92, 78, 96, 88, 90]
# 1. 对列表进行升序排序
# 2. 对列表进行降序排序
# 3. 反转列表顺序
# 4. 找出最高分和最低分
scores = [85, 92, 78, 96, 88, 90]
scores_F = scores.copy()     #此时使用cope函数重新复制一个新列表
scores_F.sort(reverse=False)
print(scores_F)

scores_T = scores.copy()      #此时使用cope函数重新复制一个新列表
scores_T.sort(reverse=True)
print(scores_T)

scores_R = scores.copy()       #此时使用cope函数重新复制一个新列表
scores_R.reverse()
print(scores_R)
print(max(scores))
print(min(scores))


#  列表推导式
# 1. 使用列表推导式生成1-10的平方列表
# 2. 使用列表推导式从[1,2,3,4,5,6,7,8,9,10]中筛选出偶数
# 3. 使用列表推导式将["apple", "banana", "cherry"]转换为大写
# 4. 使用列表推导式生成[10, 20, 30, 40, 50]中每个元素除以10的结果
li = [1,2,3,4,5,6,7,8,9,10]
li_1 =[i ** 2 for i in li]
print(li_1)
li_2 = [i for i in li if i % 2 == 0]
print(li_2)
str = ["apple","banana","cherry"]
str_1 = [i.upper() for i in str]
print(str_1)
li = [10,20,30,40,50]
li_4 = [i / 10 for i in li]
print(li_4)



#列表嵌套
# 给定嵌套列表：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 1. 访问第二个子列表 [4, 5, 6]
# 2. 访问数字5（第二行第二列）
# 3. 将数字8改为88
# 4. 在第一个子列表末尾添加数字10
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
matrix[2][1] = 88
matrix[0].append(10)
print(matrix)


#  综合练习
# 给定列表：students = ["Alice", "Bob", "Charlie", "David"]
# 1. 添加新学生 "Eve" 到列表末尾
# 2. 在 "Bob" 后面插入 "Frank"
# 3. 删除 "David"
# 4. 将列表按字母顺序排序
# 5. 检查 "Charlie" 是否在列表中
# 6. 反转列表顺序
students = ["Alice", "Bob", "Charlie", "David"]
students.append("Eve")
print(students)
print(students)
students.insert(1,"Frank")
print(students)
students.remove("David")
students.sort(reverse=False)
print(students)
print("Charlie" in students)
students.sort(reverse=True)
print(students)




