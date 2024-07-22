max_num = 0
idx = 0

for i in range(1, 10):
    n = int(input())
    if n > max_num:
        idx = i
        max_num = n

print(max_num)
print(idx)