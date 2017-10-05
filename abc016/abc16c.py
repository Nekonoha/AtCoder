N, M = map(int, input().split())

input_list = []

for i in range(M):
    input_list.append(list(map(lambda x: int(x) - 1, input().split())))

data_list = [[] for i in range(N)]

for i in range(M):
    data_list[input_list[i][0]].append(input_list[i][1])
    data_list[input_list[i][1]].append(input_list[i][0])


result = []

for i, v in enumerate(data_list):
    tmp_list = []
    for j in v:
        tmp_list = list((set(data_list[j]) | set(tmp_list)) - set(v))
        tmp_list.remove(i)
    result.append(tmp_list)

for i in result:
    print(len(i))
