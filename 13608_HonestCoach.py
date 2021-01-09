for i in range(int(input())):
    N = int(input())
    N1  = input().split()
    for i in range(N):
        N1[i]= int(N1[i])

    N1.sort(reverse=True)
    diff = N1[0]-N1[1]
    for i in range(len(N1)-1):
        if(N1[i]-N1[i+1])<diff:
            diff = N1[i]-N1[i+1]
    print(diff)

