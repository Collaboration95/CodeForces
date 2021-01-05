N = int(input())
l1 = input().split()
for i in range(0,len(l1)):
    l1[i] = int(l1[i])
small = l1[0]
pos_l = 0
pos_s = 0
large = l1[0]
for i in range(N):
    if l1[i]>large:
        large = l1[i]
        pos_l = i
    if l1[i]<=small:
        small = l1[i]
        pos_s= i
if pos_l>pos_s:
    print(pos_l+ N-pos_s-1-1)
else:
    print(pos_l+ N-pos_s-1)
