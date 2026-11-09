class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to infinity and max profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                # We found a new minimum price to buy
                min_price = price
            elif price - min_price > max_profit:
                # We found a better profit
                max_profit = price - min_price
                
        return max_profit