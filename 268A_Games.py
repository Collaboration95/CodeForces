count = 0
l = []
N = int(input())
for i in range(0,N):
    N = input().split()
    l.append(N[0])
    l.append(N[1])

for i in range(0,len(l)):
    l[i] = int(l[i])
for i in range(1,len(N),2):
    print(l[i])
    for j in range(0,len(N)):
        if l[i]==l[j] and j%2==0:
            count+=1
print(count)