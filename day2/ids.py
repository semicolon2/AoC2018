input = set(open("input.txt").readlines())


def comp(a, b):
    if a == b:
        return "a"
    return "b"


for i in input:
    for j in input:
        if i == j:
            continue
        x = list(map(comp, i, j))
        if x.count("b") == 1:
            print(i, "\n", j)
            quit
