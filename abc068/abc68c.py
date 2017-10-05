N, M = map(int, input().split())
ab_list = [list(map(lambda x: int(x) - 1, input().split())) for i in range(M)]

lis = [[] for i in range(N)]

for i in range(M):
    lis[ab_list[i][0]].append(ab_list[i][1])

que = [[0, 0, lis[0], []]]
ends = []
res = False

while que:
    count, now, next_nodes, visited = que.pop()
    visited.append(now)
    if now == N - 1:
        ends = visited[:]
    for node in next_nodes:
        if node in visited or count == 2:
            continue
        que.append([count + 1, node, lis[node], visited[:]])

if N - 1 in ends:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
