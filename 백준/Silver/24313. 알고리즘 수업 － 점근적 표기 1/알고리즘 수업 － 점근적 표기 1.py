a, b = map(int, input().split())
c = int(input())
n = int(input())

def f(x):
    global a, b
    return a * x + b

print(1 if f(n) <= c * n and c >= a else 0)