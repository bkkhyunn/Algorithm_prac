n = int(input())
cnt = 1
end = 1
if n == 1:
    print(1)
else:
    while True:
        post = end + cnt * 6
        if end < n <= post:
            break
        cnt += 1
        end = post
    print(cnt+1)