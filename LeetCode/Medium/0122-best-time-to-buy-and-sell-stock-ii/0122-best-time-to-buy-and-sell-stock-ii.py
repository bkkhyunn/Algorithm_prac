class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dynamic programming & greedy
        '''
        buy = 10 ** 4
        sub_profit = 0
        total_profit = 0
        
        for price in prices:
            buy = min(price, buy)
            profit = price - buy
            
            # 그리디에 따라, 얻을 수 있는 이익이 최대치일 때 가져간다. 하루 지나면 못 가져가기 때문.
            if sub_profit > profit:
                # 지금까지 얻을 수 있는 최대 이익을 챙기기
                total_profit += sub_profit
                # 부분 최대 이익과 구매 가격 재설정
                sub_profit, buy = 0, price

            else:
                sub_profit = max(sub_profit, profit)
        
        # 마지막에 총 이익에 부분 최대 이익 더해주기
        total_profit += sub_profit
                
        return total_profit
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''greedy'''
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
    
class Solution:
    def maxProfit(self, prices):
        '''dynamic programming'''
        
        n = len(prices)
        # hold[i]: i번째 날에 주식을 보유하고 있는 경우 최대 이익
        hold = [0] * n
        # not_hold[i]: i번째 날에 주식을 보유하고 있지 않은 경우 최대 이익
        not_hold = [0] * n
        
        hold[0] = -prices[0]  # 첫날 주식을 산 경우. 이익 입장에서 산 경우는 마이너스.
        
        for i in range(1, n):
            # hold[i] 는 아래 중 더 큰 값
            # 전날에 이미 주식을 보유하고 있었거나 (hold[i-1]),
            # 전날에 주식을 보유하지 않았다가 주식을 사는 경우 (not_hold[i-1] - prices[i])
            hold[i] = max(hold[i-1], not_hold[i-1] - prices[i])
            
            # not_hold[i] 는 아래 중 더 큰 값
            # 전날에 주식을 보유하지 않고 있었거나 (not_hold[i-1]),
            # 전날에 주식을 보유하다가 주식을 파는 경우 (hold[i-1] + prices[i])
            not_hold[i] = max(not_hold[i-1], hold[i-1] + prices[i])
        
        # 마지막 날에 주식을 보유하지 않은 상태의 최대 이익
        return not_hold[-1]