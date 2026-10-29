class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR values to reach (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Initialize the starting cell
        dp[0][0].add(grid[0][0])
        
        # Fill the first row (can only move right)
        for j in range(1, n):
            for val in dp[0][j - 1]:
                dp[0][j].add(val ^ grid[0][j])
                
        # Fill the first column (can only move down)
        for i in range(1, m):
            for val in dp[i - 1][0]:
                dp[i][0].add(val ^ grid[i][0])
                
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Combine XOR sets from top and left neighbors
                # We use a set union to avoid duplicate XOR values
                combined = dp[i - 1][j] | dp[i][j - 1]
                for val in combined:
                    dp[i][j].add(val ^ grid[i][j])
                    
        # The answer is the minimum XOR value at the bottom-right cell
        return min(dp[m - 1][n - 1])