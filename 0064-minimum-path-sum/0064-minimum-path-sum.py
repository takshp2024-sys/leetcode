class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize a 1D DP array with the first row's cumulative sums
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
            
        # Iterate through the remaining rows
        for i in range(1, m):
            # Update the first column (can only come from above)
            dp[0] += grid[i][0]
            
            # Update the rest of the columns
            for j in range(1, n):
                # dp[j] currently holds the min cost from the cell ABOVE
                # dp[j-1] holds the min cost from the cell to the LEFT
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                
        return dp[-1]