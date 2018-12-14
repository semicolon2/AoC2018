import re

input = set(open("input.txt").readlines())

claims = []

for line in input:
    i, xstart, ystart, xlength, ylength = re.findall(r"\d{1,}", line)
    claims.append({"index": i, "area": [[1 for x in range(int(xstart), int(xstart) + int(xlength))] for y in range(int(ystart), int(ystart) + int(ylength))])
