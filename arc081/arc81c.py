N = int(input())
A = sorted(list(map(int, input().split())) + [0, 0, 0, 0], reverse=True)

res = []
tmp = -1
for a in A:
    if a == tmp:
        res.append(a)
        tmp = -1
    else:
        tmp = a
    if len(res) >= 2:
        break

res = sorted(res, reverse=True)

result = 1
for i in range(2):
    result *= res[i]

print(result)
