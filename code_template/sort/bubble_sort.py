def bubble_sort(arr):
    '''
    1. 처음부터 끝까지 리스트를 순회하면서 인접한 두 원소를 비교
    2. 비교한 두 원소의 순서가 잘못되어 있으면 교환
    3. 한 번의 순회가 끝나면 가장 큰 원소가 리스트의 끝으로 이동
    4. 이를 반복하여 정렬이 완료될 때까지 수행
    '''
    n = len(arr)
    for i in range(n):
        # 마지막 i개 요소는 이미 정렬되었으므로 비교할 필요가 없습니다.
        for j in range(0, n-i-1):
            # 인접한 두 요소를 비교하여 필요에 따라 교환합니다.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 예제
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)