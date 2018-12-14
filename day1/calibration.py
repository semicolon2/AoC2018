input = [int(line) for line in open("input.txt").readlines()]

print(sum(input))

twice = False
freq = 0
seen = list()
while not twice:
    for i in input:
        freq += i
        if freq in seen:
            twice = freq
            print(twice)
            break
        seen.append(freq)
