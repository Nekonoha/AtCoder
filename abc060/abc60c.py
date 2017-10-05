N, T = map(int, input().split())
t = list(map(int, input().split()))

tmp = 0
sum_t = 0

for i in range(N-1):
    if t[i+1] - t[i] < T:
        sum_t += t[i+1] - t[i]
    else:
        sum_t += T

print(sum_t + T)
