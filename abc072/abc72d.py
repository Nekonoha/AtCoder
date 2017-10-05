N = int(input())
P = [0] + list(map(int, input().split()))

res = 0
for i in range(1, len(P)):
    if i == P[i]:
        if i == N:
            P[i], P[i - 1] = P[i - 1], P[i]
        else:
            P[i], P[i + 1] = P[i + 1], P[i]
        res += 1

print(res)
