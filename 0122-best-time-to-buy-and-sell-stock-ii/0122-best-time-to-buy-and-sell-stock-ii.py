class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        # Iterate through the array starting from the second day
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, we "buy" yesterday and "sell" today
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit