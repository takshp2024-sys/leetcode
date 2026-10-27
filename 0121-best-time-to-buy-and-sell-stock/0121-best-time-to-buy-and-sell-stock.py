class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very large number (or the first element)
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the prices
        for price in prices:
            if price < min_price:
                # We found a new lowest price to buy
                min_price = price
            elif price - min_price > max_profit:
                # We found a better profit
                max_profit = price - min_price
                
        return max_profit