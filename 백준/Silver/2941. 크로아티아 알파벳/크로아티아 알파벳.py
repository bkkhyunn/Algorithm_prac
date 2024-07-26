s = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for w in word:
    while w in s:
        s = s.replace(w, ' ', 1)
        cnt += 1

print(cnt + len(s.replace(' ', '')))