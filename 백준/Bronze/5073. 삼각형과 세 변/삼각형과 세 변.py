while True:
    a, b, c = map(int, input().split())
    if a+b+c == 0:
        break
    
    edges = [a, b, c]
    edges.sort()
    
    if edges[-1] < edges[0] + edges[1]:
        if len(set(edges)) == 1:
            print("Equilateral")
        elif len(set(edges)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")