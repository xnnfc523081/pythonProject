#  输入函数   input

input("请输入姓名：")

age = input("请输入年龄")
print(age,type(age))
# print(f'{age=}')     #查看age打印结果，加等号运行出来的结果为age='输入内容'，但python3.7不支持在f-string中使用等号
print(f"{age}")
'无论输入函数内写的什么都会默认为字符串'
'输入的数据存储到变量当中，便于后续对与数据的使用'

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  转义字符

#  1.制表符      \t       可以用来对齐文本
#  注意：四个英文字符占据一个单元格

print("w\t*")                    #1个w和\t组成一个单元格   此时\t占据三个英文字符
print("ww\t*")                   #2个w和\t组成一个单元格   此时\t占据两个英文字符
print("www\t*")                  #3个w和\t组成一个单元格   此时\t占据一个英文字符
print("wwww\t*")                 #4个w和\t组成一个单元格   此时\t独占一个单元格
print("wwwww\t*")                #5个w和\t组成一个单元格   此时\t占据三个英文字符
print("wwwwww\t*")               #6个w和\t组成一个单元格   此时\t占据两个英文字符
print("wwwwwww\t*")              #7个w和\t组成一个单元格   此时\t占据一个英文字符

#  2.换行符      \n

print("这是第一行,\n这是第二行,\n这是第三行。")

#  3.反斜杠符号      \\           两个反斜杠构成一个反斜杠用来规避语法错误

print("D:\nycharmproject\pythonBase\tythonProject")        #此时由于文件夹路径与python语法冲突，\n被转义为换行，\t被转义为制表符
print("D:\\nycharmproject\pythonBase\\tythonProject")      #此时两个反斜杠转义为一个可以正确表达文件夹路径

#  4.单双引号    \'为单引号      \"为双引号

#当内部包含双引号     如果要输出    Hello,"you are beautiful"
print("Hello,\"you are beautiful\"")
#内部包含单引号       如果要输出   Hello，'you are beautiful'
print("Hello,\'you are beautiful\'")
#既有单引号也有双引号  如果要输出"It's beautiful"
print("\"It\'s beautiful\"")

#  5.原生字符串    r""       字符串保持原样输出内容       \\的进阶版本，为了节省和简化代码可以直接使用r""原生字符来进行表达

#"C:\Users\21524\.android"      #此时\Users\215会被理解为一个整体而非普通字符串会报错

print(r"C:\Users\21524\.android")     #此时使用原生字符不改变字符串同时实现正确输出


'其他转义字符补充：https://blog.csdn.net/weixin_63779518/article/details/148581267'



