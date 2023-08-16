matrix = [['.' for _ in range(8)]for _ in range(8)]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

cors = input()    # Input of figure coordinates

x, y = letters.index(cors[0]), int(cors[1]) - 1
matrix[y][x] = 'N'    # Set the figure

for i in range(8):
    for j in range(8):
        if abs(j - x) ** 2 + abs(i - y)**2 == 5:    # Checking a possible knight move
            matrix[i][j] = '*'

for row in reversed(matrix):    # Output of the matrix
    print(*row)
