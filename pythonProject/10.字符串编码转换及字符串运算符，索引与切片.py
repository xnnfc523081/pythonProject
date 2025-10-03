#  1.ASCII编码
#  2.GB2312/GBK编码
#  3.Unicode编码（万国码）
#  3.UTF—8（可变长编码）

#  字符串编码转换   将字符串转换为字节串

#  1.encode（）编码

str = "你今天真美啊"

#  转换为utf-8类型的编码
UTF8_type = str.encode("utf-8")
#  打印编码
print(UTF8_type,type(UTF8_type))

#  转换为GBK类型的编码
gbk = str.encode("gbk")
#  打印编码
print(gbk,type(gbk))

#  2.decode（）解码

#  utf_8字节序列
utf_8 = b'\xe4\xbd\xa0\xe4\xbb\x8a\xe5\xa4\xa9\xe7\x9c\x9f\xe7\xbe\x8e\xe5\x95\x8a'
#  utf-8 解码为字符串
utf_8 = utf_8.decode("utf-8")
#  打印字符串
print(utf_8,type(utf_8))

#  GBK字节序列
GBK = b'\xc4\xe3\xbd\xf1\xcc\xec\xd5\xe6\xc3\xc0\xb0\xa1'
#  GBK解码为字符串
gbk = GBK.decode("gbk")
#  打印字符串
print(gbk,type(gbk))

'编码方式与解码方式一致，否则在解码时候会出现乱码和报错'

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  字符串运算符

# 1.字符串拼装
# 参考文献：https://blog.csdn.net/sinat_38682860/article/details/94332899

print("你" + "好")
print("美女" * 3)

# 2.成员运算符      检查字符串中是否包含了某个字符串（某个或多个）

#（1）in：如果包含返回Ture,否则返回False
a = "hello"
print("h" in a)
print("c" not in a)

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# 索引（下标）
# 作用：用于快速定位并获取字符串特定位置的元素
# 语法格式：str[index]    index是一个整数，表示要访问的字符在字符串中的位置
# 从左往右，下标从0开始
# 从右往左，下标从-1开始

name = "hello，world"     #左往右
print(name[0])
print(name[1])
print(name[2])


print(name[-1])          # 右往左
print(name[-2])
print(name[-3])
print(name[-4])


# 切片（Slice）是一种强大的操作，用于从序列（如列表、字符串、元组等）中提取部分内容
# 语法：str[start：stop：step]
# start：起始索引，表示切片开始的位置（包含该位置）。如果省略，则默认为 0。
# stop：结束索引，表示切片结束的位置（不包含该位置）。如果省略，则默认为序列的长度。
# step：步长，表示每次跳过的元素个数。如果省略，默认为 1
# step 为正，读取方向为正向
# step 为负，读取方向为负向

test = "abcdefghijklmn"

# 指定起始索引为0，结束索引为-6，步长为1
print(test[0:-6:1])

# 只指定起始索引
print(test[2:])

# 只指定结束索引
print(test[:5])

# 只指定步长
print(test[::-3])

#步长读取方向与起始索引方向一致
print(test[13:1:-3])       #从右往左读取，起始索引和结束索引为正数，步长为负数
print(test[-1:-13:-3])     #从左往右读取，起始索引和结束索引为负数，步长为负数
