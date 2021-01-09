count = 0
count1 = 0
for i in range(int(input())):
    N1 = input().split()
    N1[0],N1[1] = int(N1[0]),int(N1[1])
    if N1[0]>N1[1]:
        count+=1
    elif N1[0]<N1[1]:
        count1+=1
if count>count1:
    print("Mishka")
elif count1>count:
    print("Chris")
else:
    print("Friendship is magic!^^")