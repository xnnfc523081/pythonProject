#  练习题：使用1 2 3 4 可以组成多少个组成无重复的三位数？具体值为多少？

#定义变量存储总数
count = 0
#  遍历百位的四位数字
for a in range(1,5):
    #遍历十位的四位数字
    for b in range(1,5):
        #遍历个位的四位数字
        for c in range(1,5):
            #设置条件a不等于b不等于c这一条件
            if a != b and a != c and b != c :
                #打印具体三位数
                print(a,b,c)
                #当满足以上条件时候count自加一记录满足条件的个数
                count += 1
print(f"满足条件的个数为:{count}")


#  练习题：
#  1.打印九九乘法表

#  设置外循环行数为9行
for num in range(1,10):
    #  设置内循环列数等于行数
    for aaa in range(1,num+1):
        #  打印乘法表并且禁止换行用制表符对齐文本
        print(f"{num} × {aaa} = {num * aaa}",sep="\t",end = "\t")
    #一次外循环换行，循环9次为9行
    print()

#  2.打印所有水仙花及其个数
#  要求第一个数的三次方加第二个数字的三次方加第三位数字的三次方等于第一位第二位第三位数字连在一起，这就是一个水仙花
sum = 0
for d in range(1,10):
    for e in range(0,10):
        for f in range(0,10):
            ddd = d * 100 + e * 10 + f
            total = d ** 3 + e ** 3 + f ** 3
            if ddd == total:
                print(f"水仙花为:{ddd}")
                sum += 1
print(f"水仙花个数为：{sum}")

#  3.猴子吃桃
#  猴子第一天摘了若干个桃子，当天吃了一半，又多吃了一个，第二天又吃掉一半，又多吃了一个，以后每天都吃前一天剩下桃子的一半零一个，到第十天
#  想吃的时候就剩下了一个
remaining = 1
for day in range(9,0,-1):
    remaining = (remaining * 2 + 1)
print(f"第一天的桃子数量：{remaining}")






