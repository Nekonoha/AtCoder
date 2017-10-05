N, M = map(int, input().split())

A = [input() for i in range(N)]
B = [input() for i in range(M)]

res = False
count = 0
for i in range(N - M + 1):
    if res:
        break
    for j in range(N - M + 1):
        count = 0
        for m in range(M):
            if A[i + m][j:j + M] != B[m]:
                res = False
                break
            else:
                count += 1
        if count == M:
            res = True
            break

if res:
    print("Yes")
else:
    print("No")
