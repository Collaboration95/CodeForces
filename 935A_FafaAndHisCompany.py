count = 0
n = int(input())
for i in range(1,n+1):
    if (n-i)%i==0:
        count+=1
print(count-1)
