N = input().split()
N[0],N[1] = int(N[0]),int(N[1])
if N[0]>N[1]:
    N[0],N[1] = N[1],N[0]
str1 =""

str1+=str(N[0])
str1 += " "
if (N[1]-N[0])>1:
    str1+= str((N[1]-N[0])//2)
else:
    str1+="0"
print(str1)