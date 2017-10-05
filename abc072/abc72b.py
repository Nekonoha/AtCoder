S = input()

res = ""

for i, v in enumerate(S):
    if i % 2 == 0:
        res += v

print(res)
