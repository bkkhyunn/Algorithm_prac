'''
- 슬라이딩 윈도우 알고리즘은 고정 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘이다.
    -  배열이나 리스트와 같은 자료구조에서 연속된 부분의 합이나 평균, 최대/최소값 등을 구할 때 유용하다.
- 교집합의 정보를 공유하고, 차이가 나는 양쪽 끝 원소만 갱신하는 방법이다.
- 배열이나 리스트의 요소의 일정 범위의 값을 비교할 때 사용하면 매우 유용하다.
- 투 포인터(two poitners) 알고리즘과 연동하여 많이 쓰인다.
    - 1차원 배열이 있고 이 배열에서 각자 다른 원소를 가리키는 2개의 포인터를 조작하며 원하는 값을 얻는 형태
- 투 포인트 알고리즘은 구간의 넓이가 조건에 따라 유동적으로 변하며, 슬라이딩 윈도우 알고리즘은 항상 구간의 넓이가 고정되어 있다는 차이점이 있다.

- 동작과정
    1. 처음 k 개의 요소의 합을 계산하여 초기 윈도우의 합으로 설정한다.
    2. 배열을 순회하면서 윈도우를 오른쪽으로 한 칸씩 옮길 때마다 새로운 요소를 더하고 이전 요소를 빼서 새로운 윈도우의 합을 계산한다.
    3. 각 윈도우의 합을 결과 리스트에 추가한다.
'''

def sliding_window_sum(arr, k):
    """
    Args:
    - arr (list): 입력 배열
    - k (int): 윈도우 크기

    Returns:
    - list: 윈도우 크기 k의 부분 배열의 합 리스트
    """
    n = len(arr)
    if n < k:
        return []

    window_sum = sum(arr[:k])
    result = [window_sum]

    for i in range(n - k):
        window_sum += arr[i + k] - arr[i]
        result.append(window_sum)

    return result

# 테스트
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(sliding_window_sum(arr, k))  # 출력: [6, 9, 12, 15, 18, 21, 24, 27]
