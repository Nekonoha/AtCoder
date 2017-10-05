N = int(input())
A = list(map(int, input().split()))

L = []
res = "No"

for a in A:
    if a % 4 == 0:
        L.append(4)
        continue
    elif a % 2 == 0:
        L.append(2)
        continue
    else:
        L.append(1)

if L.count(2) == 0:
    if L.count(1) <= (L.count(4) + 1):
        res = "Yes"
elif L.count(1) <= L.count(4):
    res = "Yes"

print(res)
