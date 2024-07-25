stdin = input().split()
d, start = int(stdin[0]), stdin[1]
alphabet = list('abcdefghijklmnopqrstuvwxyz')
dic = {}
max_length = 0
max_length_word = ''

for _ in range(d):
    word = input()
    dic[word] = False
dic[start] = True
def dfs(word):
    global max_length, max_length_word
    l = len(word)
    
    if l > max_length:
        max_length = max(max_length, l)
        max_length_word = word
    
    for s in alphabet:
        for i in range(l+1):
            new_word = word[:i] + s + word[i:]
            
            if new_word in dic:
                if not dic[new_word]:
                    dic[new_word] = True
                    dfs(new_word)
dfs(start)
print(max_length_word)