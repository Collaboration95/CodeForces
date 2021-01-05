N = input()
str1 = N[1:-1]

l = []
for i in str1:
    if i!="," and i!=" ":
        l.append(i)

if len(set(l))==0:
    print(0)
else:
    print(len(set(l)))