N, Q = map(int, input().split())

map = [list(map(lambda x: int(x)-1, input().split())) for q in range(Q)]

p = [0 for i in range(N+1)]

#いもす法で処理
for m in map:
    p[m[0]] += 1
    p[m[1]+1] -= 1

result = ""

# 累積和をだす　奇数解ひっくり返した場合は白　偶数なら黒
for i in range(N):
    p[i+1] += p[i]
    result += str(p[i]%2)

print(result)



