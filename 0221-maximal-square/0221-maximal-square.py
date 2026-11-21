class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] stores the side length of the largest square ending at (i, j)
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # If on the edge, the max square side is 1
                        dp[i][j] = 1
                    else:
                        # The side length is 1 + the minimum of the three adjacent squares
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                        
                    # Update the maximum side length found so far
                    max_side = max(max_side, dp[i][j])
                    
        # The area is the square of the side length
        return max_side * max_side