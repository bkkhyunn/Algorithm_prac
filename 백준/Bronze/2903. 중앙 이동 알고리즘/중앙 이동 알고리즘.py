n = int(input())
dot = 4
edge = 4
rect = 1

for i in range(1, n+1):
    dot += (edge + rect)
    rect *= 4
    edge = int(rect ** 0.5) * 4 + int(rect ** 0.5) * int(rect ** 0.5 - 1) * 2
    
print(dot)