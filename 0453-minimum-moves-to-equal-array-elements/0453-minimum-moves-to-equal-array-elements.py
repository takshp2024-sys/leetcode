class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # The minimum number of moves is the sum of the differences 
        # between each element and the minimum element in the array.
        min_val = min(nums)
        
        moves = 0
        for num in nums:
            moves += num - min_val
            
        return moves