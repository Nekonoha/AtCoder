a, b, c = map(int, input().split())

result = "NO"

for i in range(a, a*b+a, a):
    if i % b is c:
        result = "YES"
        break

print(result)