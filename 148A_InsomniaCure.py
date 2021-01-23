k,l,m,n,d =  int(input()),int(input()),int(input()),int(input()),int(input())
set1 = set()
if (d>=k and d>=m and d>=l and d>=n):
    for i in range(1,d+1):
        if (i%k==0):
            set1.add(i)
        elif(i%l==0):
            set1.add(i)
        elif(i%m==0):
            set1.add(i)
        elif(i%n==0):
            set1.add(i)
print(len(set1))
