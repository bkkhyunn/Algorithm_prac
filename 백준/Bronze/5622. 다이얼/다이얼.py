string = list(input())
alphabet = [chr(i) for i in range(65, 91)]
num = list('22233344455566677778889999')
dic = {}
for a, n in zip(alphabet, num):
    dic[a] = int(n)
answer = 0
for s in string:
    answer += dic[s] + 1
    
print(answer)