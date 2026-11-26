class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s at the beginning and end
        arr = [1] + nums + [1]
        n = len(arr)
        
        # dp[i][j] represents the maximum coins we can get by bursting all balloons
        # strictly between index i and index j (exclusive).
        dp = [[0] * n for _ in range(n)]
        
        # We iterate over the length of the interval
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                
                # Try bursting every balloon 'k' as the LAST balloon in the interval (i, j)
                for k in range(i + 1, j):
                    coins = arr[i] * arr[k] * arr[j]
                    total = coins + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
                    
        return dp[0][n - 1]