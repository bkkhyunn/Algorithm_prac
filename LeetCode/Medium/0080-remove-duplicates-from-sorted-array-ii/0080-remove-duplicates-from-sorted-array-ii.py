from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count_dict = Counter(nums)
        
        for n in list(set(nums)):
            
            while count_dict[n] > 2:
                nums.remove(n)
                count_dict[n] -= 1
        
        return len(nums)