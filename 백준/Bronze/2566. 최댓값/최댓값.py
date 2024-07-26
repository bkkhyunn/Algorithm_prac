matrix = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
coord = (1, 1)
for i in range(9):
    for j in range(9):
        if max_value < matrix[i][j]:
            max_value = matrix[i][j]
            coord = (i+1, j+1)
            
print(max_value)
print(f'{coord[0]} {coord[1]}')