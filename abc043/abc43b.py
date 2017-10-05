S = list(input())

result = []

for s in S:
    if s in ("0", "1"):
        result.append(s)
    elif result:
        result.pop()

print("".join(result))
