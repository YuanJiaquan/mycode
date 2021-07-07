# 1、用print函数打印多个值
print(123456)

# 2、用print函数不换行打印
print('hello')
print('hello \nworld')

# 3、导入模块的方式有哪些
import selenium.webdriver
from selenium import webdriver
# import class02.demo2

# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？

# 可变数据类型：列表，集合字典
# 不可变数据类型：数字，字符串，元祖


# 5、分别对49.698作如下打印
# 	1）四舍五入，保留两位小数
# 	2）向上入取整
# 	3）向下舍取整
# 	4）计算8除以5返回整型
# 	5）求4的2次幂
# 	6）返回一个（1,100）随机整数
import math
a=49.698
print(round(a,1))
print(math.ceil(a))
print(8//5)
print(pow(4,2))
import random
print(random.randrange(0,100))

# 6、依次对变量a,b,c赋值为1,2,3
a,b,c=1,2,3
# 7、截取某字符串中从2索引位置到最后的字符子串
s=input()
print(s[2::1])
# 8、对字符串“testcode”做如下处理：
# 	1）翻转字符串
print(s[::-1])
# 	2）首字母大写
print(s.capitalize())
# 	3）查找是否包含code子串，并返回索引值
try:
    print(s.index('asd'))
except  Exception  as e:
    print(e)
# 	4）判断字符串的长度
print(len(s))
# 	5）从头部截取4个长度字符串
print(s[:4:1])
# 	6）把code替换为123
print(s.replace('code','123'))
# 	7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理
str1="test code"
b=str1.split('')
print(b)
# 9、讲小数转为整数
x=4.255
y=int(x)
# 10、如何打印出字符串“test\ncode”
print(r'test\ncode')
# 以下可慢点写：
# 11、按逗号分割列表当中的元素 list=[1,2,3,4,5,6]  输出1，2，3，4，5，6
l1=[1,2,3,4,5,6]
l2=[str(i) for i in l1]
print(",".join(l2))
# 12、字符串"Hey, you - what are you doing here!?" 分割成'Hey', 'you', 'what', 'are', 'you', 'doing', 'here'
import re
s1="Hey, you - what are you doing here!?"
s2=re.findall(r'[A-Za-z]+',s1)
print(','.join(s2))