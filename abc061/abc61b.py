n, m = map(int, input().split())

ab_list = [list(map(lambda x: int(x) - 1, input().split())) for i in range(m)]

result_list = [[] for i in range(n)]

for ab in ab_list:
    result_list[ab[0]].append(ab[1])
    result_list[ab[1]].append(ab[0])


for result in result_list:
    print(len(result))
