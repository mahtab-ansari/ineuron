list1 = []
for x in range(2000,3201):
    if (x % 7 == 0) and (x % 5 != 0):
        list1.append(x)

st = ''
for i in range(0,len(list1)-1):
    st+=str(list1[i])+','
#print(st)

st+=str(list1[len(list1)-1])
print(st)