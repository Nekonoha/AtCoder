n, m = map(int, input().split())

std_map = [list(map(int, input().split())) for i in range(n)]
ch_map = [list(map(int, input().split())) for i in range(m)]

results = [[] for i in range(n)]

for std in std_map:
    print(min(enumerate([abs(std[0] - ch[0]) + abs(std[1] - ch[1]) for ch in ch_map], 1), key=lambda x: x[1])[0])
