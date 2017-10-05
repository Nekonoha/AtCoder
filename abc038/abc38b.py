HW1 = set(map(int, input().split()))
HW2 = set(map(int, input().split()))

res_len = len(HW1) + len(HW2)
res = HW1 | HW2

if res_len is len(res):
    print("NO")
else:
    print("YES")