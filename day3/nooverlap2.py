import re

input = set(open("input.txt").readlines())

grid = [[set() for x in range(1000)] for y in range(1000)]

for line in input:
    i, xstart, ystart, xlength, ylength = re.findall(r"\d{1,}", line)
    for x in range(int(xstart), int(xstart) + int(xlength)):
        for y in range(int(ystart), int(ystart) + int(ylength)):
            grid[x][y].add(int(i))

claims = set(range(1, 1374))
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if len(grid[x][y]) > 1:
            for i in grid[x][y]:
                claims.discard(i)
print(claims)
