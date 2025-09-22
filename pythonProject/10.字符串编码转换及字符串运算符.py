#  1.ASCII编码
#  2.GB2312/GBK编码
#  3.Unicode编码（万国码）
#  3.UTF—8（可变长编码）


#  字符串编码转换

#  1.encode（）编码

#  字符串内容       str类型
str = "你今天真美啊"
#  转换为utf-8类型的编码
UTF8_type = str.encode("utf-8")
#  打印编码
print(UTF8_type,type(UTF8_type))


#  2.decode（）解码

#  utf_8字节序列    byte类型
utf_8 = b'\xe4\xbd\xa0\xe4\xbb\x8a\xe5\xa4\xa9\xe7\x9c\x9f\xe7\xbe\x8e\xe5\x95\x8a'
#  utf-8 解码为字符串
st = utf_8.decode("utf_8")
#  打印字符串
print(str,type(str))

'在数据转换时，必须确保使用的编码方式与原始的编码方式相匹配，否则会导致数据损坏或解码失败'