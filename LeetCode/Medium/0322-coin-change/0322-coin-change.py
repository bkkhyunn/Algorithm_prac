# 각 coins 들을 보면, 큰 단위가 작은 단위의 배수가 아니기 때문에 그리디 로는 최적의 해가 보장되지 않는다.
# DP 중 bottom-up 방식 이용
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp 테이블. 각 인덱스는 amount 를 나타내며, 값은 그 amount 를 만들 때 사용할 수 있는 가장 최소의 동전 수를 나타낸다.
        dp = [0] + ([float('inf')] * amount)
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]