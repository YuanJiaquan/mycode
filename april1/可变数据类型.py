# 1、定义一个列表[1, 2, 3]，并将列表中的头尾两个元素对调。对调后为[3, 2, 1]
l1=[1,2,3]
l1[0],l1[2]=l1[2],l1[0]
print(l1)

# 2、定义一个列表，并将列表中的指定位置的两个元素对调。对调第一个和第三个元素
# 列表如下：[23, 65, 19, 90]
# 对调后结果：[19, 65, 23, 90]
l2=[23, 65, 19, 90]
l2[0],l2[2]=l2[2],l2[0]
print(l2)

# 3、对列表[10, 11, 12, 13, 14, 15]
# 翻转，调整后为[15, 14, 13, 12, 11, 10]
l3=[10, 11, 12, 13, 14, 15]
l3.reverse()
print(l3)
# 4、判定6是否包含列表[1, 6, 3, 5, 3, 4]
l4=[1, 6, 3, 5, 3, 4]
for i in l4:
    if i==6:
        print(True)
    else:
        pass

# 5、[1, 6, 3, 5, 3, 4]
# 转换为元组
l5=[1, 6, 3, 5, 3, 4]
t5=(tuple(l5))
print(t5)

# 6、根据列表[1, 6, 3, 5, 3, 4]
# 作为新字典的key, 对应key的初始值为0，并打印新字典对象
l6=[1, 6, 3, 5, 3, 4]
d6={}
d61=d6.fromkeys(l6,0)

# 7、循环打印出字典
# {'name': 'aming', 'age': 18, 'school': 'cema'}
# 中的所有键和值，
d7={'name': 'aming', 'age': 18, 'school': 'cema'}
for i in d7:
    print(i,d7[i])


# 8、{‘taobao’, 'jingdong', 'alibaba', 'baidu', 'taobao'}对元素去重复  （不做）
a={'taobao', 'jingdong', 'alibaba', 'baidu', 'taobao'}
print(set(a))
for i in set(a):
    print(i)

# 9、分别有两个集合
# {1, 2, 1, 3, 4, 5, 6, 7}，{1, 2, 3, 8, 9, 7, 10}，求两个集合的差集、并集、交集（不做）
x={1, 2, 1, 3, 4, 5, 6, 7}
y={1, 2, 3, 8, 9, 7, 10}
print(x&y)
print(x|y)
print(x-y)
print(x^y)
# 10、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复
if x&y:
    print(x&y)
else:
    print(x-y)

# 11、list7 = [1, 2, 3, 4, 5]
# 根据列表中的元素作为字典中的key, 及初始值为0，打印这个新的字典，不用fromkey方法实现
list7 = [1, 2, 3, 4, 5]
d11={}
print(d11.fromkeys(list7,0))
# 12、把元组转为字符串
t12=(1,2,3)
print(str(t12),type(str(t12)))

# 13、字典转为字符串，字符串转为字典
d13={'name': 'aming', 'age': 18, 'school': 'cema'}
s=str(d13)
dx=eval(s)
print(s,type(s))
print(dx,type(dx))
