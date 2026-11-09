class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the states to represent the maximum profit at each stage.
        # We use float('-inf') for buy states to represent that we haven't bought yet.
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        
        for price in prices:
            # 1. First buy: Max of previous buy1 or buying at the current price
            buy1 = max(buy1, -price)
            
            # 2. First sell: Max of previous sell1 or selling the first bought stock
            sell1 = max(sell1, buy1 + price)
            
            # 3. Second buy: Max of previous buy2 or buying using the profit from sell1
            buy2 = max(buy2, sell1 - price)
            
            # 4. Second sell: Max of previous sell2 or selling the second bought stock
            sell2 = max(sell2, buy2 + price)
            
        return sell2