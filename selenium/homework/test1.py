l=[1,5,68,8,5,2,6,10,11]
l1=[1,68,8,6,10,11]
l3=l
l4=[]
for i in l1:
    for j in l:
        if i==j:
            l3.remove(i)
print(l3)


