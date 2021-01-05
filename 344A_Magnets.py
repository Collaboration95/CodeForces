count= 0
N = int(input())
star1= ""
j = 0
for i in range(N):
    str1 = input()

    while j:
        star1 = str1
        j = 0

    if star1==str1:
        pass
    else:
        count+=1
        star1=str1
print(count)