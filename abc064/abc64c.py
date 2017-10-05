N = int(input())
a = list(map(int, input().split()))

res_min = 0
res_max = 0

g = list(filter(lambda x: x <= 399, a))
br = list(filter(lambda x: 400 <= x <= 799, a))
gr = list(filter(lambda x: 800 <= x <= 1199, a))
s = list(filter(lambda x: 1200 <= x <= 1599, a))
bl = list(filter(lambda x: 1600 <= x <= 1999, a))
y = list(filter(lambda x: 2000 <= x <= 2399, a))
o = list(filter(lambda x: 2400 <= x <= 2799, a))
r = list(filter(lambda x: 2800 <= x <= 3199, a))
t = list(filter(lambda x: 3200 <= x, a))

c_list = [g, br, gr, s, bl, y, o, r]

for c in c_list:
    if len(c) != 0:
        res_min += 1
        res_max += 1

if res_min == 0:
    res_min += 1
res_max += len(t)


print(res_min, res_max)
