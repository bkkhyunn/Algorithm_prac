a = int(input())
b = input()
answer = 0

for i, n in enumerate(b[::-1]):
    print(a * int(n))
    answer += (a * int(n+('0'*i)))
print(answer)