#  变量

#  1.直接给变量赋值
money = 10000
print(money)

#  2.把一个变量赋值给另一个变量
money2 = money
print(money2)

#  3.将运算结果赋值给变量
money3= 1000+1000
print(money3)

#  4.同一个变量可以反复赋值
#  如果赋值多个变量，且没有在赋值后打印那个，以最终打印的以最后一个为准
num = 1
print(num)
num = 2
print(num)
num = "123"
print(num)

#  5.变量规则:https://blog.csdn.net/weixin_45693433/article/details/144122948

# (1)下划线分割法
employee_id = "1"
print(employee_id)

# (2)大驼峰格式命名
MyName = "2"
print(MyName)

# (3)小驼峰格式命名
myName = "3"

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  标识符 可由数字字母下划线中文括号组成（不推荐中文和括号命名）   数字不可以放在开头    不能有空格   不能使用纯括号和半个括号

#  字母下划线
_user = "andi"
print(_user)

#  数字下划线
_1 = "hhh"
print(_1)

#  字母数字
zihan1 = "hhhh"
print(zihan1)

#  中文
姓名 = "sy"
print(姓名)

#  括号字母
(qq) = "hhh"
print(qq)

#  中文字母下划线数字
h哈_1 = "冰冰"
print(h哈_1)

#标识符命名规则:https://blog.csdn.net/qq_40997679/article/details/149674539



#  PY编程关键字
import keyword
print(keyword.kwlist)









