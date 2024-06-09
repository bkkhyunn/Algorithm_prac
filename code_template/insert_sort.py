array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번째 원소부터 시작
    for j in range(i, 0, -1): # 인덱스 i 부터 0 까지 1씩 감소하며 반복
        if array[j] < array[j-1]: # 왼쪽 원소와 비교
            array[j], array[j-1] = array[j-1], array[j] # 스와핑
        else: # 자기보다 작거나 같은 데이터를 만나면 그 위치에서 멈춘다.
            break

## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]