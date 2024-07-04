from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_dict = defaultdict(int)
        for n in nums:
            n_dict[n] += 1
            
        return max(n_dict, key=lambda x: n_dict[x])