N, M = map(int, input().split())

man = [0, 0, 0]

res = False

if M % 2 == 1:
    man[1] = 1

man[0] = N - man[1]
man[2] = N - man[0] - man[1]

while True:
    if man[0] < 0:
        man = [-1, -1, -1]
        break
    if man[0] * 2 + man[1] * 3 + man[2] * 4 == M:
        break
    man[0] -= 1
    man[2] = N - man[0] - man[1]

print(*man)
