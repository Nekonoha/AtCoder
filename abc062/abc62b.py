h, w = map(int, input().split())

image = ["".join(["#"] + input().split() + ["#"]) for i in range(h)]
image.insert(0, "#"*(w+2))
image.append("#"*(w+2))

for i in image:
    print(i)
