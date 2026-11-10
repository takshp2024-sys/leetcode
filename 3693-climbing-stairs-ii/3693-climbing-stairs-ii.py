class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Edge case: if n is 0, we are already at the destination
        if n == 0:
            return 0
            
        # dp[i] represents the min cost to reach step i.
        # We only need the last 3 values, so we use three variables.
        # dp0 = cost to reach step 0, dp1 = step 1, dp2 = step 2
        dp0 = 0
        dp1 = float('inf')
        dp2 = float('inf')
        
        for i in range(1, n + 1):
            # Calculate the minimum cost to reach the current step i
            # We can jump from i-1, i-2, or i-3
            
            # Cost from i-1
            cost_from_1 = dp0 + costs[i - 1] + 1
            
            # Cost from i-2 (if i >= 2)
            cost_from_2 = dp1 + costs[i - 1] + 4 if i >= 2 else float('inf')
            
            # Cost from i-3 (if i >= 3)
            cost_from_3 = dp2 + costs[i - 1] + 9 if i >= 3 else float('inf')
            
            # The minimum cost to reach step i
            current_dp = min(cost_from_1, cost_from_2, cost_from_3)
            
            # Shift the variables for the next iteration
            dp2 = dp1
            dp1 = dp0
            dp0 = current_dp
            
        return dp0