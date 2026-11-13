class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # dp[i][j] represents the minimum health required to reach the bottom-right corner from (i, j)
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # If we are at the bottom-right corner
                if i == m - 1 and j == n - 1:
                    # We need at least 1 health after taking the damage/gain
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                # If we are at the last row (can only move right)
                elif i == m - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                # If we are at the last column (can only move down)
                elif j == n - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                # General case (choose the path that requires less health)
                else:
                    min_health_next = min(dp[i + 1][j], dp[i][j + 1])
                    dp[i][j] = max(1, min_health_next - dungeon[i][j])
                    
        return dp[0][0]