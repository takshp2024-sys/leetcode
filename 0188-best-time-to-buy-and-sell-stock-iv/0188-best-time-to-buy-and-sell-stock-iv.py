class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
            
        n = len(prices)
        
        # If k is large enough, the problem reduces to "Best Time to Buy and Sell Stock II"
        # Because you can't make more than n//2 transactions
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit
            
        # dp_buy[t] = maximum profit after the t-th buy
        # dp_sell[t] = maximum profit after the t-th sell
        # Initialize with a very small number for buy (representing a large negative cost)
        dp_buy = [float('-inf')] * (k + 1)
        dp_sell = [0] * (k + 1)
        
        for price in prices:
            for t in range(1, k + 1):
                # The maximum profit after the t-th buy is either:
                # 1. The previous state of buying t times
                # 2. The profit from t-1 sells minus the current price
                dp_buy[t] = max(dp_buy[t], dp_sell[t - 1] - price)
                
                # The maximum profit after the t-th sell is either:
                # 1. The previous state of selling t times
                # 2. The profit from buying t times plus the current price
                dp_sell[t] = max(dp_sell[t], dp_buy[t] + price)
                
        return dp_sell[k]