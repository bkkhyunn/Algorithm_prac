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
    
