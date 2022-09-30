class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = prices[-1]
        profit = 0
        for i in range(len(prices) - 1, -1, -1):
            profit = max(profit, largest - prices[i])
            largest = max(largest, prices[i])
        return profit
            
        
        
        
        
        
        
        
        
        
        # I: list of prices on ith day
        # O: max profit or 0 if no profit
        # C: n/a
        # E: no profit or no stocks to trade?