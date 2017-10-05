N = int(input())
A = [int(input()) for i in range(N)]

p = {v: i for i, v in enumerate(sorted(list(set(A))))}

for a in A:
    print(p[a])
