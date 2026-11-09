class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start with the bottom row of the triangle as our initial DP array
        dp = triangle[-1]
        
        # Iterate upwards from the second-to-last row to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # The minimum path sum from this node is its value plus the 
                # minimum of the two adjacent nodes directly below it
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        # The top element will hold the overall minimum path sum
        return dp[0]