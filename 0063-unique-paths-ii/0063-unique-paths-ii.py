class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting cell or ending cell has an obstacle, there are 0 paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
            
        # Initialize the DP array for the first row
        dp = [0] * n
        dp[0] = 1
        
        # Process the first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[j] = dp[j - 1]
            else:
                dp[j] = 0  # Obstacle blocks the path
                
        # Process the remaining rows
        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Obstacle resets the path count for this cell
                elif j > 0:
                    # dp[j] currently holds the paths from the cell ABOVE
                    # dp[j-1] holds the paths from the cell to the LEFT
                    dp[j] = dp[j] + dp[j - 1]
                    
        return dp[-1]