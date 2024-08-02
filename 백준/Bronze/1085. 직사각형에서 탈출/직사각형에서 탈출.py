x, y, w, h = map(int, input().split())

print(min(min(x-0, w-x), min(y-0, h-y)))