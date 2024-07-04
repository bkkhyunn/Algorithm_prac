class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10 ** 4
        max_profit = 0
        total_profit = 0
        for price in prices:
            buy = min(price, buy)
            profit = price - buy
            if max_profit > profit:
                total_profit += max_profit
                max_profit = 0
                buy = price
            else:
                max_profit = max(max_profit, profit)
        total_profit += max_profit
                
        return total_profit