N = int(input())

res_list = []
tmp = 1
while True:
    if tmp > N:
        break
    res_list.append(tmp)
    tmp *= 2


print(max(res_list))