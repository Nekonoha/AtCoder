N = int(input())
A = list(map(int, input().split()))

L = [0 for i in range(max(A) + 10)]

for a in A:
    L[a] += 1
    L[a - 1] += 1
    L[a + 1] += 1

print(max(L))
