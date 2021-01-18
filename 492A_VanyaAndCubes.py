# loop = 0
# sum = 0
# sum1= 0
# N = int(input())
# while True:
#     if N>sum:
#         for i in range(loop):
#             sum+=i
#             print(sum)
#         if N<sum:
#             print(loop)
#             break
#         loop+=1
#     else:
#         print(loop)
#         break
N = int(input())
sum = 0
loop = 0
while True:
    loop +=1
    for i in range(loop+1):
        sum +=i

    if N>sum:
        continue
    elif N==sum:
        print(loop)
        break
    else:
        print(loop-1)
        break