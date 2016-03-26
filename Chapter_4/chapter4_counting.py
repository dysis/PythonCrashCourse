numbers = range(1, 21)
for number in numbers:
    print(number)

million = range(1, 1000001)
print(sum(million))
print(min(million))
print(max(million))

odds = range(1, 20, 2)
for odd in odds:
    print(odd)

threes = range(3, 31, 3)
for three in threes:
    print(three)

cubes = range(1, 11)
for cube in cubes:
    print(cube**3)

compcubes = [compcube**3 for compcube in range(1,11)]
print(compcubes)