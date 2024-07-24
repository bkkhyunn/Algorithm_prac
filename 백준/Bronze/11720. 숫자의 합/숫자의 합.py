import sys

input = sys.stdin.readline

n = int(input())
s = input()
answer = 0

for i in range(n):
    answer += int(s[i])
    
print(answer)