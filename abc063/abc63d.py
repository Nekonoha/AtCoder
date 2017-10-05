import math
n, a, b = map(int, input().split())
h = [int(input()) for i in range(n)]

result = 0
tmp = 0
# while(len(h) != 0):
#     h.sort()
#     if h[0]//a == 0:
#         tmp = 1
#     else:
#         tmp = h[0]//a
#     h[0] -= tmp*a
#     for i in range(1, len(h)):
#         h[i] -= tmp*b
#     h = list(set(h) - set(filter(lambda x : x <= 0, h)))
#     result += tmp


print(result)