n, x = map(int, input().split())
nums = list(map(int, input().split()))
answer = []

for num in nums:
    if num < x:
        answer.append(str(num))
        
print(' '.join(answer))