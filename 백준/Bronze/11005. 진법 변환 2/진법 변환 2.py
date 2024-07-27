n, b = map(int, input().split())
char = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''
while n > 0:
    s = char[n % b] + s
    n //= b

print(s)