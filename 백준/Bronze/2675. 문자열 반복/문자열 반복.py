n = int(input())

for _ in range(n):
    answer = ''
    repeat, string = input().split()
    for s in string:
        answer += (s * int(repeat))
    print(answer, end='\n')
    
