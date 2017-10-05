n = int(input())
Sn = [input() for i in range(n)]

res = []


for s in Sn:
    res = sorted(list(set(s) or set(res)))

result = ""
for r in res:
    tmp = 10000
    for s in Sn:
        tmp = min(tmp, s.count(r))
    result += r*tmp

print(result)
