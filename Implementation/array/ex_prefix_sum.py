def prefix_sum(arr):
    """
    주어진 배열의 prefix sum 배열(누적합)을 계산하는 함수

    Args:
    - arr (list): 입력 배열

    Returns:
    - list: prefix sum 배열
    """
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

# 테스트
arr = [1, 2, 3, 4, 5]
print(prefix_sum(arr))  # 출력: [1, 3, 6, 10, 15]
