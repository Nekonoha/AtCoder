N = int(input())
S = list(input())

v = []
tmp = []

for s in S:
    if s == "(":
        tmp.append(")")
        v.append("(")
    else:
        if len(tmp) == 0:
            v.insert(0, "(")
            v.append(")")
        else:
            v.append(tmp.pop())

while tmp:
    v.append(tmp.pop())

print("".join(v))
