import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        n_merged = np.array(merged)
        return np.median(n_merged)