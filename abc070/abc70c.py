N = int(input())
T = [int(input()) for n in range(N)]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


res = T[0]
for t in T:
    res = lcm(res, t)

print(res)
