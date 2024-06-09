# 재귀 함수로 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    # 찾은 경우 중간점 인덱스 반환. mid 가 찾고자 하는 값의 인덱스라고 할 수 있다.
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
# 반복문으로 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
            
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 라이브러리 이용 이진 탐색 구현
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) ## 2
print(bisect_right(a, x)) ## 4


# 값이 특정 범위에 속하는 데이터 개수 구하기
# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
    
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # 2

# 값이 -1 부터 3 까지 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6