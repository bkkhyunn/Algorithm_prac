from collections import Counter
s = input().upper()
dic = Counter(list(s))
max_cnt, max_s = 0, ''
for i in dic.keys():
    if max_cnt < dic[i]:
        max_cnt = dic[i]
        max_s = i

if list(dic.values()).count(max_cnt) > 1:
    print("?")
else:
    print(max_s)