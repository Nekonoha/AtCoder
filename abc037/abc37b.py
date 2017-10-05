N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for i in range(Q)]
list = [0 for i in range(N)]

for q in range(Q):
    for i in range(LRT[q][0]-1, LRT[q][1]):
        list[i] = LRT[q][2]

for res in list:
    print(res)
