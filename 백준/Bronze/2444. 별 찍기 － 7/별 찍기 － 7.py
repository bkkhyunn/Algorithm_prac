n = int(input())
l = 2*n - 1
for i in range(1, n+1):
    star = "*" * (2*i - 1)
    print("{:^{}}".format(star, l).rstrip())

for i in range(n-1, 0, -1):
    star = "*" * (2*i - 1)
    print("{:^{}}".format(star, l).rstrip())