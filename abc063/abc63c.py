n = int(input())

s = [int(input()) for i in range(n)]

sum_s = sum(s)
not_list = [num for num in s if num % 10 != 0]


if sum_s % 10 == 0:
    if len(not_list) == 0:
        sum_s = 0
    else:
        sum_s -= sorted(not_list)[0]

print(sum_s)