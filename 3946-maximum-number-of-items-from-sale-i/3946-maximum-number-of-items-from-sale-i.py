class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # Precompute the free items for each item
        free_items_count = [0] * n
        for i in range(n):
            factor_i = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    free_items_count[i] += 1
                    
        # dp[b] will store the maximum items we can get with exactly or at most budget b
        dp = [0] * (budget + 1)
        
        # First, handle the "first copy" of each item (0/1 Knapsack style)
        # We iterate backwards to ensure we only pick each item's first copy once
        for i in range(n):
            cost = items[i][1]
            value = 1 + free_items_count[i]
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + value)
                
        # Next, handle buying additional copies (Unbounded Knapsack style)
        # We iterate forwards to allow multiple copies of the same item
        for i in range(n):
            cost = items[i][1]
            value = 1
            for b in range(cost, budget + 1):
                dp[b] = max(dp[b], dp[b - cost] + value)
                
        # The answer is the maximum items we can get with at most 'budget'
        return max(dp)