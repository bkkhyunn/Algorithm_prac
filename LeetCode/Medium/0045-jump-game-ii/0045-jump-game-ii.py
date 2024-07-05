class Solution:
    def jump(self, nums: List[int]) -> int:
        ''' greedy & dynamic programming '''
        
        # index 별 최소로 점프했을 때 횟수
        dp = [10**4] * len(nums)
        dp[0] = 0
        
        for i, num in enumerate(nums):
            for j in range(1, num+1):
                if i+j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i]+1)
                
        return dp[-1]