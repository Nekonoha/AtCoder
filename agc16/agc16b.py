N = int(input())
a = list(map(int, input().split()))

result = True

if len(set(a)) > 1:
    set_min = list(set(a))[0]
    set_max = list(set(a))[1]

    if len(set(a)) > 2:
        result = False
    elif (set_max - set_min) != 1:
        result = False
    else:
        if set_max == N-1:
            result = (a.count(set_min) == N-2)
        else:
            result = (a.count(set_min) < set_max)
else:
    result = (list(set(a))[0] <= N/2 or list(set(a))[0] == N-1)



if result:
    print("Yes")
else:
    print("No")
