class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the maximum value in the array
        max_val = max(nums)
        
        # Calculate the sum of differences between the maximum and each element
        moves = 0
        for num in nums:
            moves += max_val - num
            
        return moves