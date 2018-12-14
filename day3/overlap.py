import re

input = set(open("input.txt").readlines())

grid = [[0 for x in range(1000)] for y in range(1000)]
overlaps = 0

for line in input:
    _, xstart, ystart, xlength, ylength = re.findall(r"\d{1,}", line)
    for x in range(int(xstart), int(xstart) + int(xlength)):
        for y in range(int(ystart), int(ystart) + int(ylength)):
            grid[x][y] += 1
            if grid[x][y] == 2:
                overlaps += 1
print(overlaps)
