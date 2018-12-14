input = set(open("input.txt").readlines())

alphabet = "abcdefghijklmnopqrstuvwxyz"
two = 0
three = 0

for i in input:
    for letter in alphabet:
        if i.count(letter) == 2:
            two += 1
            break
    for letter in alphabet:
        if i.count(letter) == 3:
            three += 1
            break
print(two)
print(three)
print(two * three)
