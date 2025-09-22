#  数据类型
#  type()  获取数据类型

#  1.整型（int）   存储整数变量

num1 = 10000
print(type(num1))
print(num1,type(num1))

#  2.浮点型（float）   存储小数变量

num2 = 3.14
print(type(num2))
print(num2,type(num2))

#  3.布尔型（bool）    使用真（True），假（False）来进行判断    区分大小写

V1 = True
print(V1,type(V1))

V2 = False
print(V2,type(V2))

"""布尔型在运算中隐式为整型    True为1   False为0"""

QQ = True + 1   #Ture被当作1处理
print(QQ)

Result = False * 4
print(Result)

#  4.复数型（complex）    实数+虚数  虚部后面跟j/J  可以大小写  在复数中为固定的虚数单位不可更改

Complex = 1 + 2j
print(Complex,type(Complex))

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  字符串（str）
#  带有引号（单引号双引号三引号）用来存储和表达文本信息  三引号适用于包含多行内容的字符串

#  定义字符串类型的变量

#  单引号界定

p1 = 'hello word'
print(p1,type(p1))

#  双引号界定

p2 = "wordexcel"
print(p2,type(p2))

#  三引号界定（多行字符串）   可以双引号也可以单引号

p3 = '''
这是一个多行
单引号字符串
'''
print(p3,type(p3))

p4 = """
这是一个多行
双引号字符串
"""
print(p4,type(p4))

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#格式化输出
#  1.%操作符  旧版字符串格式化  不推荐

#  2.str.format()   新式字符串格式化

name = "冰冰"
age = 18
sex = "女"
print("我的姓名是{},我的年龄是{},我的性别是{}".format(name,age,sex))
#指定关键数数字
print("我的姓名是{n},我的年龄是{a},我的性别是{s}".format(n=name,a=age,s=sex))



#  3.f—strings   在字符串前加上f或F来标识，在字符串内嵌入表达式，表达式被大括号包围，计算结果被转换为字符串插入到相应位置
#    f—strings支持在python内嵌入任意表达式

name = "冰冰"
age = 18
sex = "女"
print(f"我的姓名是{name},我的年龄是{age},我的性别是{sex}")
print(F"我的姓名是{name},我的年龄是{age},我的性别是{sex}")


num = 32
num1 = 12
print(f"3×4={num * num1}")
#  4.设置整数位数

sid = 1
aid = 123
print(f"我的学号为{sid:3d}")      #设置为三位数不足三位数前面补空格
print(f"我的学号为{sid:03d}")     #设置为三位数不足三位数前面补0
print(f"我的学号为{sid:003d}")    #设置为三位数不足三位数前面补0


#  5.保留小数精度

p = 3.141597653589793
print(f"pi取五位小数：{p:.5f}")     #保留五位小数。超过五位四舍五入，不足五位数则后面补0
aa = 3.14
print(f"aa取三位小数：{aa:.3f}")

#  6. 控制小数精度和宽度    需要用到%占位符     举例：% 精度要求 %被要求精度的变量

jac = 8.33555
print("对数字宽度精度进行限制: %9d.3f" %jac)

apk = 8.12345565
print("对数字精度宽度进行限制: %5d.5f" %apk)











