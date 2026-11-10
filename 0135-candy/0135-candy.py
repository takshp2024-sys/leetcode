class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # Initialize each child with 1 candy (the minimum required)
        candies = [1] * n
        
        # Left-to-Right pass: compare with the left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # Right-to-Left pass: compare with the right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # We take the max to ensure both left and right conditions are satisfied
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        # Return the total number of candies
        return sum(candies)