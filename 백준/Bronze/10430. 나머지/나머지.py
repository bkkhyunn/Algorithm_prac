a, b, c = map(int, input().split())

print((a+b)%c, end='\n')
print(((a%c)+(b%c))%c, end='\n')
print((a*b)%c, end='\n')
print(((a%c)*(b%c))%c)