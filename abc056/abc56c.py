X = int(input())

tmp = 0
res = 0
for i in range(1, X+1):
    if tmp >= X:
        break
    res = i
    tmp += i

print(res)