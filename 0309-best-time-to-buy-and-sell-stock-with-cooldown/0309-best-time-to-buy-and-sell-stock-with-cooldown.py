class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # Initial states for day 0
        hold = -prices[0]  # We bought on day 0
        sold = 0           # Cannot have sold on day 0
        rest = 0           # Not holding, not in cooldown
        
        for i in range(1, len(prices)):
            price = prices[i]
            
            # CRITICAL: Save the previous day's states BEFORE updating
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            # Update states based on PREVIOUS day's values
            # Hold: Either keep holding, or buy today (must have been in 'rest' yesterday)
            hold = max(prev_hold, prev_rest - price)
            
            # Sold: We must sell today (must have been holding yesterday)
            sold = prev_hold + price
            
            # Rest: Either keep resting, or we just finished cooldown from yesterday's sell
            rest = max(prev_rest, prev_sold)
            
        return max(sold, rest)