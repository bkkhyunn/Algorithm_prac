def find_median_sorted_arrays(nums1, nums2):
    """
    두 개의 정렬된 배열의 중앙값을 찾는 함수

    Args:
    - nums1 (list): 첫 번째 정렬된 배열
    - nums2 (list): 두 번째 정렬된 배열

    Returns:
    - float: 두 배열의 중앙값
    """
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        return merged[n//2]

# 테스트
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))  # 출력: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(find_median_sorted_arrays(nums1, nums2))  # 출력: 2.5
