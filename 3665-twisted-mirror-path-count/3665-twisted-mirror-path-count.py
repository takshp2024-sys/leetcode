class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Precompute the final destination of a move from every cell.
        # right_dest[i][j] = (r, c) where the robot ends up if it moves right from (i, j)
        # down_dest[i][j] = (r, c) where the robot ends up if it moves down from (i, j)
        # We use -1 to denote an invalid move (moves out of bounds).
        
        right_dest = [[-1] * n for _ in range(m)]
        down_dest = [[-1] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Determine right move destination
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        right_dest[i][j] = (i, j + 1)
                    else:
                        # Mirror: moving right enters (i, j+1) and turns down.
                        # So the robot ends up at down_dest[i][j+1]
                        right_dest[i][j] = down_dest[i][j + 1]
                
                # Determine down move destination
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        down_dest[i][j] = (i + 1, j)
                    else:
                        # Mirror: moving down enters (i+1, j) and turns right.
                        # So the robot ends up at right_dest[i+1][j]
                        down_dest[i][j] = right_dest[i + 1][j]
                        
        # DP table to count paths
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                    
                # Try moving right
                if j + 1 < n:
                    dest = right_dest[i][j]
                    if dest != -1:
                        r, c = dest
                        dp[r][c] = (dp[r][c] + dp[i][j]) % MOD
                        
                # Try moving down
                if i + 1 < m:
                    dest = down_dest[i][j]
                    if dest != -1:
                        r, c = dest
                        dp[r][c] = (dp[r][c] + dp[i][j]) % MOD
                        
        return dp[m - 1][n - 1]