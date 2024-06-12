n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1,2,3,2,5] # 전체 수열

count = 0
# 부분 수열의 부분 합
interval_sum = 0
end = 0

# start 를 차례대로 증가시키며 반복
for start in range(n):
    # end 를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m 일 때 카운트 증가
    if interval_sum == m:
        count += 1
    # while 문을 빠져나올 때는 interval_sum 이 m 보다 크기 때문에 start 값을 빼준다.
    interval_sum -= data[start]