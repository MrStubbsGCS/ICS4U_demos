import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

grid = []
length = 7

for i in range(length):
    grid.append([])
    for j in range(length):
        letter = random.randint(0,25)
        grid[i].append(alphabet[letter])

    print(grid[i])



