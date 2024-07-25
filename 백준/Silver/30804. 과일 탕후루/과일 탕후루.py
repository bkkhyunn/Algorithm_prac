n = int(input())
stick = list(map(int, input().split()))

start, end = 0, 0
max_length = 0
fruit_count = {}

while end < n:
    # 현재 과일의 개수를 증가
    if stick[end] in fruit_count:
        fruit_count[stick[end]] += 1
    else:
        fruit_count[stick[end]] = 1

    # 두 종류 이하의 과일로 유지되는 구간이 될 때까지 start를 이동
    while len(fruit_count) > 2:
        fruit_count[stick[start]] -= 1
        if fruit_count[stick[start]] == 0:
            del fruit_count[stick[start]]
        start += 1

    # 현재 구간의 길이를 계산
    max_length = max(max_length, end - start + 1)
    end += 1

print(max_length)