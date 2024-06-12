# 데이터의 개수 N 과 데이터
n = 5
data = [10,20,30,40,50]

# Prefix Sum 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])