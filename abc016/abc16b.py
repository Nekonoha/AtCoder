a, b, c = map(int, input().split())
p = a + b
m = a - b
pp = False
mm = False

if p == c:
    pp = True
if m == c:
    mm = True

if pp and mm:
    print("?")
elif pp:
    print("+")
elif mm:
    print("-")
else:
    print("!")
