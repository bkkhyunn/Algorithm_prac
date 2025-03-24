'''
병합 정렬
1. 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
3. 각 부분 리스트를 재귀적으로 병합 정렬을 이용해 정렬한다.
4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 병합한다.
'''

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 중간 지점을 계산
        left_half = arr[:mid]  # 왼쪽 부분 배열
        right_half = arr[mid:]  # 오른쪽 부분 배열

        merge_sort(left_half)  # 왼쪽 부분 배열을 재귀적으로 정렬
        merge_sort(right_half)  # 오른쪽 부분 배열을 재귀적으로 정렬
        
        # i: left_half 배열의 현재 위치를 나타내는 인덱스
        # j: right_half 배열의 현재 위치를 나타내는 인덱스
        # k: 원래 배열 (arr)의 현재 위치를 나타내는 인덱스
        i = j = k = 0

        # 좌우 부분 배열을 병합
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 왼쪽 부분 배열에 남은 요소들 복사
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 오른쪽 부분 배열에 남은 요소들 복사
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 예제
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)