N = int(input())
a = map(int, input().split())

a = sorted(a, reverse=True)

result = 0

for i in range(N - 1):
    result += a[i] - a[i + 1]

print(result)
