coin = [25, 10, 5, 1]
use = [0, 0, 0, 0]

t = int(input())

for _ in range(t):
    m = int(input())
    
    for i, c in enumerate(coin):
        a, b = divmod(m, c)
        m = b
        use[i] = a

    for u in use:
        print(u, end=' ')