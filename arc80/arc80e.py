from operator import itemgetter

N = int(input())
p = list(map(int, input().split()))
PE = {}
PO = {}
P = {}

for n in range(N):
    P[n] = p[n]


for n in range(0, N - 1, 2):
    PE[n] = P[n]
    PO[n + 1] = P[n + 1]

res = ""

print(res)
