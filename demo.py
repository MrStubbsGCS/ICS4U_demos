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

listWords = ["word1", "word2", "word3", "word4", "word5", "word6"]
newList = []
for i in listWords:
    randomI = random.randint(0, 5)
    while listWords[randomI] in newList:
        randomI = random.randint(0, 5)
    newList.append(listWords[randomI])

print(newList)




