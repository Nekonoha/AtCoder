N = int(input())
NG = [int(input()) for i in range(3)]
res = False

if N not in NG:
    for i in range(100):
        if N - 3 not in NG and N - 3 >= 0:
            N -= 3
        elif N - 2 not in NG and N - 2 >= 0:
            N -= 2
        elif N - 1 not in NG and N - 1 >= 0:
            N -= 1
        else:
            break

    if N == 0:
        res = True

if res:
    print("YES")
else:
    print("NO")
