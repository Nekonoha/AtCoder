import itertools

O = list(input())
E = list(input())

print("".join(itertools.chain(*zip(O, E))) + (O[-1] if len(O) is not len(E) else ""))
