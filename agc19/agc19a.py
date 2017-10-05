Q, H, S, D = map(int, input().split())
N = int(input())

H = min(Q * 2, H)
S = min(H * 2, S)
D = min(S * 2, D)

res = 0

if S <= D/2:
    res = N * S
else:
    res = ((N // 2) * D) + ((N % 2) * S)

print(res)
