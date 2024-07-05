class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        dynamic programming
        시간복잡도가 O(N^2) 지만,
        nums[i] 가 1000 보다 작기 때문에 가능하다.
        '''
        
        # index 별 최소로 점프했을 때 횟수
        dp = [10**4] * len(nums)
        dp[0] = 0
        
        for i, num in enumerate(nums):
            for j in range(1, num+1):
                if i+j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i]+1)
                
        return dp[-1]
    
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        greedy
        시간복잡도 O(N) 으로 풀 수 있다.
        
        1. 배열을 순회하면서 각 인덱스 i에서 가능한 가장 먼 위치를 계산하고 farthest를 업데이트
        2. 인덱스 i가 점프할 수 있는 범위의 끝에 도달하면 최소 점프 횟수를 증가시키고,
        다음 점프 범위로 이동
        3. 마지막 인덱스에 도달하거나 그 이상으로 갈 수 있는 경우, 루프를 종료하고 점프 횟수를 반환
        '''
        
        n = len(nums)
        # 최소 점프 횟수
        jumps = 0
        # 현재 인덱스에서 도달할 수 있는 가장 먼 위치
        farthest = 0
        # 전 인덱스에서 도달한 가장 먼 위치
        end = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
                if end >= (n-1):
                    break

        return jumps