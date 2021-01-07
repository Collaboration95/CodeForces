
l = [int(x) for x in input().split()]

l.sort()
L = [l[-1]-x for x in l[:-1]]
str1 =""
for i in range(len(L)):
    str1+=str(L[i])
    str1+=" "

print(str1[:-1])