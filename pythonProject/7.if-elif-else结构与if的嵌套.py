#  1.if-else结构     条件成立执行if条件下的缩进代码，如果不成立执行else下的缩进代码     二选一

age = 19                   #定义一个变量
if age >=18 :              #写判断语句 如果age大于等于18则执行缩进代码块
    print("您已经成年")
else:                      #如果不符合判断为假，则执行else语句下的代码块
    print("未成年")

#  三元表达式（条件表达式）   适用于简单代码  复杂逻辑代码不适用有难度

age = 16
print("您已经成年") if age >=18 else print("未成年")

#  2.if-elif结构     在多个条件中进行选择,只有第一个满足条件的分支会被执行(多选一),跳过剩下的elif和else及其对应的代码块

weather = "snowy"                 #定义一个变量
if weather == "sunny":            #判断语句如果天气为sunny则执行缩进代码块
    print("今天天气为sunny")
elif weather == "cloudy":         #判断语句如果天气为cloudy则执行缩进代码块,不满足跳过
    print("今天天气为coludy")
elif weather == "rainy":          #判断语句如果天气为rainy则执行缩进代码块,不满足跳过
    print("今天天气为rainy")
elif weather == "snowy":          #判断语句如果天气为snowy则执行缩进代码块,不满足跳过
    print("今天天气为snowy，天气不好")

#  3.if-elif-else结构     elif分支必须跟在if/elif语句后不然会报错

#  需求：使用if-elif-else结构判断天气状况

weather = "unknow"                #定义一个变量
if weather == "sunny":            #判断语句如果天气为sunny则执行缩进代码块
    print("今天天气为sunny")
elif weather == "cloudy":         #判断语句如果天气为cloudy则执行缩进代码块,不满足跳过
    print("今天天气为coludy")
elif weather == "rainy":          #判断语句如果天气为rainy则执行缩进代码块,不满足跳过
    print("今天天气为rainy")
elif weather == "snowy":          #判断语句如果天气为snowy则执行缩进代码块,不满足跳过
    print("今天天气为snowy，天气不好")
else:                             #前面条件都不满足则直接执行else语句
    print("不好意思天气未知")


#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  if嵌套

#  需求：运用if嵌套评估学生的学分和出勤率来选出获得奖学金的学生

score = 70                                                             #定义一个整型变量记录学生学分
attendence = 55                                                        #定义一个整型变量记录学生出勤率（百分比）
if score >= 70:                                                        #判断语句判断学分是否合格如果合格则为真执行嵌套代码
    print("该学生学分合格")
    if 0 <= attendence <20:                                            #判断出勤率是否合格，如果真则执行缩进语句，假则执行elif语句
        print("出勤率不合格")
    elif 20 <= attendence <= 90:                                       #判断在出勤率合格情况下会不会获得奖学金
        print("出勤率合格但不会获得奖学金")
    else :                                                              #前面两次判断都为假那么出勤率一定为优秀获得奖学金
        print("该学生出勤率学分都合格且优秀获得奖学金")
else:                                                                  #学分不合格直接执行缩进语句
    print("学分不合格未获得奖学金")



