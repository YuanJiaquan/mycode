import random
l=[]
for i in range(1,101):
    l.append(i)
for x in range(10):
    a3=random.sample(l,1)
    print('三等奖：%s'%a3)
    for q in l:
        if q==a3[0]:
            l.remove(q)
for y in range(5):
    a2=random.sample(l,1)
    print('二等奖：%s'%a2)
    for q in l:
        if q==a2[0]:
            l.remove(q)
for x in range(1):
    a1=random.sample(l,1)
    print('一等奖：%s'%a1)
    for q in l:
        if q==a1[0]:
            l.remove(q)








