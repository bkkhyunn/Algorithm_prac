from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count_dict = Counter(nums)
        
        for n in list(set(nums)):
            
            while count_dict[n] > 1:
                nums.remove(n)
                count_dict[n] -= 1
        
        return len(nums)
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''two pointer'''
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        #print(nums)
        return j