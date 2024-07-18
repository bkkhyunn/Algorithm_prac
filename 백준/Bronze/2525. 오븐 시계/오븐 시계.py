h, m = map(int, input().split())
t = int(input())

hh, mm = divmod(t+m, 60)

if h + hh < 24:
    print(f"{h+hh} {mm}")
else:
    print(f"{(h+hh)-24} {mm}")