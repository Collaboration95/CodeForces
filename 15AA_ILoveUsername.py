count = 0
N = int(input())
N1 =input().split()
for i in range(N):
    N1[i] = int(N1[i])
lowest = N1[0]
highest = N1[0]
for i in range(N):
    if N1[i]>highest:
        highest=N1[i]
        count+=1
    if N1[i]<lowest:
        lowest=N1[i]
        count+=1
print(count)