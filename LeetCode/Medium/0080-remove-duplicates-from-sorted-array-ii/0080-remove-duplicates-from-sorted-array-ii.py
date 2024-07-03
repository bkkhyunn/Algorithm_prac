from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count_dict = Counter(nums)
        
        for n in list(set(nums)):
            
            while count_dict[n] > 2:
                nums.remove(n)
                count_dict[n] -= 1
        
        return len(nums)
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''two pointer'''
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j