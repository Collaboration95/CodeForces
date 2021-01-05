N = int(input())
str1 = ""
for i in range(1,N+1):
    if(i!=N):
        if i%2!=0:
            str1+="I hate that "
        else:
            str1+="I love that "
    else:
        if i%2!=0:
            str1+="I hate it"
        else:
            str1+="I love it"

# if N%2==0:
#     str1+="that I love it"
# else:
#     str1 += "that I hate it"
print(str1)