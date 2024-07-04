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
        ''' two pointer '''
        
        # 0, 1 idx 는 최대 중복 허용이 2회기 때문에 확인하지 않아도 된다.
        # point 는 중복이 제거된 배열의 인덱스를 뜻한다.
        point = 2
        
        # nums 를 앞에서부터 중복을 제거한 배열로 탈바꿈 시킨다.
        for i in range(2, len(nums)):
            if nums[i] != nums[point-2]:
                nums[point] = nums[i]
                point += 1
                
        return point