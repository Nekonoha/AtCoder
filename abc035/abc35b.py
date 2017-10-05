S = input()
T = int(input())

L = S.count('L')
R = S.count('R')
U = S.count('U')
D = S.count('D')
Q = S.count('?')

now_map = [[0, abs(R-L)], [3, abs(U-D)]]

if T == 1:
    now_map = sorted(now_map, key=lambda x: x[1], reverse=True)
    now_map[0][1] += Q
else:
    for i in range(Q):
        now_map = sorted(now_map, key=lambda x: x[1], reverse=True)
        now_map[0][1] -= 1
        now_map[0][1] = abs(now_map[0][1])

now_map = sorted(now_map, key=lambda x: x[0])
result = abs(now_map[0][1]) + abs(now_map[1][1])

print(result)
