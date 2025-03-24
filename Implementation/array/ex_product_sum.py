def product_except_self(nums):
    """
    주어진 배열의 각 요소에 대해 자신을 제외한 모든 요소의 곱을 계산하는 함수

    Args:
    - nums (list): 입력 배열

    Returns:
    - list: 자신을 제외한 모든 요소의 곱 배열
    """
    n = len(nums)
    result = [1] * n

    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# 테스트
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # 출력: [24, 12, 8, 6]
