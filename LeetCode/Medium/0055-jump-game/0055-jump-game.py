class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        dynamic programming
        1. dp[i] 는 i 인덱스에서 시작해서 마지막 인덱스까지 도달할 수 있는지를 나타내는 dp table
        2. dp[0] 은 항상 True. 왜냐하면 시작 인덱스에서는 이미 도달한 상태이기 때문
        3. 각 인덱스 i에 대해, i에서 가능한 모든 점프를 반복문으로 수행하면서 dp[i]가 True인 경우 dp[i + jump]를 True로 설정
        4. 마지막 인덱스의 dp 값이 True인 경우 도달할 수 있음을 의미
        
        반복문이 2번 중첩되어 O(N**2) 이기 떄문에 시간 초과 판정
        '''
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = True

        return dp[-1]
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        greedy
        1. max_reachable 는 현재까지 도달할 수 있는 최대 인덱스
        2. 배열을 순회하면서 i 가 max_reachable 보다 크면 도달할 수 없음을 의미하므로 False를 반환
        3. 그렇지 않으면, i 에서 도달할 수 있는 최대 인덱스(i + reachable)를 업데이트
        4. 배열의 모든 요소를 순회한 후 반복이 끝나면 마지막 인덱스에 도달할 수 있음을 의미하므로 True를 반환
        '''
        
        max_reachable = 0
        
        for i, reachable in enumerate(nums):
            
            if i > max_reachable:
                return False
            
            max_reachable = max(max_reachable, i + reachable)
            
        return True
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        greedy & dynamic programming
        1. dp table 은 각 인덱스에서 도달할 수 있는 최대 위치를 저장
        2. dp[0]을 nums[0]으로 초기화
        3. 배열의 각 인덱스를 순회하면서, 이전 인덱스에서 현재 인덱스까지 도달할 수 있는지를 확인
        4. 만약 도달할 수 없다면 False를 반환
        5. 도달할 수 있다면 각 인덱스에서 도달할 수 있는 최대 위치를 업데이트
        6. 마지막 인덱스에 도달할 수 있는지 확인
        '''
        n = len(nums)
        if n == 1:
            return True

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if dp[i-1] < i:
                return False
            dp[i] = max(dp[i-1], i + nums[i])

        return dp[n-1] >= n - 1