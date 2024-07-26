from collections import Counter
n = int(input())
group = n

for _ in range(n):
    s = input()
    spell = Counter(list(s))
    
    for key in spell.keys():
        if spell[key] > 1:
            if key * spell[key] in s:
                continue
            else:
                group -= 1
                break
print(group)