A = list(input())
B = list(input())
C = list(input())
esult = ""


def pop_card(s):
    global result
    if s == "a":
        if (A):
            pop_card(A.pop(0))
        else:
            result = "A"
    elif s == "b":
        if (B):
            pop_card(B.pop(0))
        else:
            result = "B"

    elif s == "c":
        if (C):
            pop_card(C.pop(0))
        else:
            result = "C"


pop_card("a")
print(result)
