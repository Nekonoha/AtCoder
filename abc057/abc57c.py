import math

N = int(input())

result_set = []

for i in range(1, int(pow(N, 0.5)) + 1):
    if N % i == 0:
        result_set.append([i, N // i])

result = pow(10, 10)

for i in result_set:
    result = min(result, int(math.log10(max(i)) + 1))


print(result)