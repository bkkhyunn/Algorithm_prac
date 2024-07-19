total = int(input())
n = int(input())
cal = 0
for _ in range(n):
    price, cnt = map(int, input().split())
    cal += (price * cnt)
if total == cal:
    print('Yes')
else:
    print('No')