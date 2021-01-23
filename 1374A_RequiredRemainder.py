for i in range(int(input())):
    N = input().split()
    print(int(N[0])*((int(N[2])-int(N[1]))//int(N[0]))+int(N[1]))
    # simplified exp print((x*(n-y)//x) +(y))