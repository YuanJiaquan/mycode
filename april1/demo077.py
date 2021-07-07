# 正则：
# 用来处理字符串
# 特点：灵活性特别强

# 导入正则

# 匹配规则：\d 匹配数字  \D
# \w字母，数字，下划线，中文
# .匹配任意字符，除\n以外
# {}前面的元素出现的次数
# ？非贪婪模式 匹配1个或者0个表达式
# +匹配1个或者多个表达式
# *匹配0个或者多个表达式
import re
# 常用的方法：match（）只匹配开头 search()只匹配一次  findall（）
# str1='123.,.,.,wowo?开始123'
# 想要把数字匹配出来,没匹配出来会是一个none,匹配出来是个对象
# a=re.match('\d+',str1).group()
# print(a)

# a=re.search('\d+',str1).group()
# print(a)

# a=re.findall('\d+',str1)
# print(a)

# 我想要匹配数字字母都想匹配?不匹配
#
# a=re.findall('\w+',str1)
# print(a)


# 12、字符串"Hey, you - what are you doing here!?" 分割成
# 'Hey', 'you', 'what', 'are', 'you', 'doing', 'here'
# str2="Hey, you - what are you doing here!?"
# print(re.findall(r'\w+',str2))


# re1=re.search('e.*a','abcde123a123a')
# # e123a     e123a123a  贪婪模式
# print(re1)
#
# re1=re.search('e.*?a','abcde123a123a')
# # e123a     e123a123a  贪婪模式
# print(re1)

# img2="<img src='test.jpg' width='20px' height='30px'>"
# re1=re.search('src=.*? ',img2).group()
# print(re1)

# 递归：函数内部自己调用自己  递归：顾名思义：有去有回

# 递归需要又个出口，没有出口会造成死循环

# def sum_number(num):
#     # 必须有个出口，当某个条件满足时，不在执行这个函数
#     if num==1:
#         return 1
#     sum_number(num-1)
#
# sum_number(3)
import  pysnooper


# 递归算法：1+2+3
@pysnooper.snoop()
def sum_number(num):
    # 必须有个出口，当某个条件满足时，不在执行这个函数
    if num==1:
        return 1
    temp=sum_number(num-1)
    return temp+num
a=sum_number(3)
print(a)

# sum_number(3)爷爷 3+3  sum_number(2)爸爸 1+ 2=3   sum_number(1)儿子 退出 返回1
# 有去有回
