import math

up, down, v = map(int, input().split())

if up >= v:
    print(1)
else:
    day = math.ceil((v-up) / (up-down)) + 1
    print(day)
