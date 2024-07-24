import sys
input = sys.stdin.readline

string = input().rstrip()
alphabet = [-1] * 26

for i, s in enumerate(string):
    if alphabet[ord(s)-97] == -1:
        alphabet[ord(s)-97] = i
    
for a in alphabet:
    print(a, end=' ')