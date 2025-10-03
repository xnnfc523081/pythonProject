# 查找练习
# 给定字符串：text = "Hello, welcome to Python world!"
# 1. 查找 "welcome" 第一次出现的位置（从开头开始查找）
# 2. 查找 "o" 在位置5之后第一次出现的位置（从索引5开始查找，包含索引5）
# 3. 统计 "o" 在整个字符串中出现的次数（从开头到结尾）
# 4. 统计 "l" 在前15个字符中出现的次数（从索引0到索引14，不包含索引15）
text = "Hello, welcome to Python world!"
print(text.find("welcome"))
print(text.find("o",5))
print(text.count("o"))
print(text.count("l",0,15))


#替换分割练习
# 给定字符串：sentence = "I love apples, apples are my favorite fruit"
# 1. 将第一个 "apples" 替换为 "oranges"（只替换第一次出现的）
# 2. 将所有 "apples" 替换为 "bananas"（替换所有出现的）
# 3. 用空格分割字符串（分割所有空白字符）
# 4. 用逗号分割字符串，只分割一次（生成2个元素的列表）
sentence = "I love apples, apples are my favorite fruit"
print(sentence.replace("apples","oranges",1))
print(sentence.replace("apples","bananas"))
print(sentence.split())
print(sentence.split(",",1))


#清理和转换练习
# 给定字符串：dirty_text = "   Hello, World!   "
# 1. 去除首尾所有空白字符（空格、换行符、制表符等）
# 2. 将字符串转换为全小写字母
# 3. 将字符串转换为全大写字母
# 4. 给定字符串：messy_text = "xxxHello Pythonxxx"，去除首尾的所有 'x' 字符
dirty_text = "   Hello, World!   "
messy_text = "xxxHello Pythonxxx"
print(dirty_text.strip())
print(dirty_text.lower())
print(dirty_text.upper())
print(messy_text.strip("x"))


#判断练习
# 1. 检查 "hello.py" 是否以 ".py" 结尾（整个字符串的结尾）
# 2. 检查 "main.py" 是否以 "main" 开头（整个字符串的开头）
# 3. 检查 "HELLO" 是否所有字母字符都是大写（至少有一个字母字符）
# 4. 检查 "hello" 是否所有字母字符都是小写（至少有一个字母字符）
# 5. 检查 "Hello123" 是否所有字母字符都是小写（数字不影响判断）
print("hello.py".endswith(".py"))
print("main,py".startswith("main"))
print("HELLO".isupper())
print("hello".islower())
print("Hello123".islower())


#综合练习
# 给定字符串：data = "   USERNAME,John Doe,AGE,25,CITY,New York   "
# 1. 去除首尾所有空白字符
# 2. 用逗号分割字符串成列表（分割所有逗号）
# 3. 检查清理后的字符串是否以 "USERNAME" 开头（从索引0开始）
# 4. 将 "John Doe" 转换为全大写字母
# 5. 统计清理后字符串中逗号 "," 出现的总次数
data = "   USERNAME,John Doe,AGE,25,CITY,New York   "
data_1 = data.strip()
data_2 = data_1.split(",")
print(data_1.startswith("USERNAME"))
print("John Doe".upper())
print(data.strip().count(","))

