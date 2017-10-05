S = input()
C_to_C = "WBWBWWBWBWBW"

now = S.find(C_to_C)
str = ""
if now % 11 is (0):
    str = "Do"
elif now % 11 is 1:
    str = "Si"
elif now % 11 in (2, 3):
    str = "La"
elif now % 11 in (4, 5):
    str = "So"
elif now % 11 in (6, 7):
    str = "Fa"
elif now % 11 is 8:
    str = "Mi"
elif now % 11 in (9, 10):
    str = "Re"

print(str)
