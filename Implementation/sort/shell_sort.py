def shell_sort(arr):
    '''
    1. 리스트의 길이의 절반을 초기 간격으로 설정. 생성된 부분 리스트의 개수는 간격(gap)과 같다.
    2. 현재 간격으로 리스트를 부분 리스트로 나누고, 각 부분 리스트를 삽입 정렬로 정렬
    3. 간격을 줄여가며(보통 간격을 절반으로 줄임) 다시 부분 리스트를 정렬한다.
    4. 간격이 1이 되면, 리스트 전체를 삽입 정렬로 정렬하여 정렬을 완료한다.
    '''
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# 예제
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = shell_sort(arr)
print("Sorted array:", sorted_arr)