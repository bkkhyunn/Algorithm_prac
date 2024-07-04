class Solution:
    def maxProfit(self,prices):
        ''' two pointer '''
        buy_idx = 0
        sell_idx = 1
        max_profit = 0
        
        while sell_idx < len(prices):
            
            profit = prices[sell_idx] - prices[buy_idx]
            
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                buy_idx = sell_idx
                
            sell_idx += 1
            
        return max_profit