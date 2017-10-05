X = input()

count = 0
t_count = 0
for x in X:
    if x == "S":
        count += 1
    if x == "T":
        count -= 1
        if count < 0:
            count = 0
            t_count += 1


print(t_count + count)
