
k = input().split()
k[0],k[1]=int(k[0]),int(k[1])
var1 = k[0]
count = 0
if k[0]%10==0:
    print(1)
elif k[0]%10==k[1]:
    print(1)
else:
    while True:
        count +=1
        if (k[0]*count)%10==0:
            print(count)
            break
        elif (k[0]*count)%10 ==k[1]:
            print(count)
            break





