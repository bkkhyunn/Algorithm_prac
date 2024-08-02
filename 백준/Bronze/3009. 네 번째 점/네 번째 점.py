coord = []

for _ in range(3):
    a, b = map(int, input().split())
    coord.append((a, b))

coord.sort()

if (coord[0][0] - coord[1][0]) != 0:
    h = coord[2][1] - coord[1][1]
    if coord[0][1] == coord[2][1]:
        print(f"{coord[0][0]} {coord[0][1] - h}")
    else:
        print(f"{coord[0][0]} {coord[0][1] + h}")
else:
    h = coord[1][1] - coord[0][1]
    if coord[2][1] == coord[1][1]:
        print(f"{coord[2][0]} {coord[2][1] - h}")
    else:
        print(f"{coord[2][0]} {coord[2][1] + h}")