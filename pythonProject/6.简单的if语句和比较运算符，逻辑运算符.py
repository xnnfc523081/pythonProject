#  简单if语句
#条件为真（True）时候执行缩进代码，条件为假（False）时候不执行代码

tep = 30          #数据
if tep > 10 :     #条件
    #如果条件为真则执行缩进代码
    print("天气较热请保持凉爽")

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  运算符

'比较运算符'

#  1.等于  ==       如果两边值相等返回True，否则返回False

print(1 == 1)             #数字比较
print('a' == 'a')         #字母比较
print('@ == @')           #符号比较

#  2.不等于   ！=

print(5 != 3)
print('a' != 'a')
print('^' != '&')

#  3.大于   >

print(5 > 6)

#  4.小于  <

print(1 < 2)

#  5.大于等于  >=

print(5 >= 5)

#  6.小于等于  <=

print(7 <= 6)

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

'逻辑运算符'

#  1.and与/且     当所有条件为True时才为真，否则为False     and只能用来连接两个或多个布尔表达式    有一个为False结果就为False

print(True and False)
print(True and True)
print(False and False)

x = 9          #被转化为布尔表达式False
y = 20         #被转化为布尔表达式True
z = 1          #被转化为布尔表达式True
print(x >=10 and y > 10 and z < 5)

#  2.or或         一个为True那么结果就为True

print(True or False)
print(True or True)
print(False or False)

x = 9
y = 20
z = 1
print(x >=10 or y > 10 or z < 5)

#  3.not非/否

print(not False)
print(not True)

xx = 11
print(not x == 10)

# 拓展  当数据为空或者0时被当作条件使用时候化为False处理    非零非空即为Ture
A = "123"
if A:
    print("真")

B = ""
if B:
    print("假")

#  4.and or 短路行为

#  只要有一个0/空，则结果为假返回0，否则结果为最后一个非0的数据

print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 2)
print(2 and 1)

#  or运算符

#  只要有一个非0/非空的，结果就返回为真的第一个数字，否则返回0

print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 2)
print(2 or 1)


