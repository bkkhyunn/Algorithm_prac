a, b, c = map(int, input().split())

if len(set([a, b, c])) == 3:
    print(max([a, b, c]) * 100)
elif len(set([a,b,c])) == 1:
    print(10000 + a * 1000)
else:
    if a == b:
        print(1000 + a * 100)
    elif a == c:
        print(1000 + a * 100)
    else:
        print(1000 + b * 100)