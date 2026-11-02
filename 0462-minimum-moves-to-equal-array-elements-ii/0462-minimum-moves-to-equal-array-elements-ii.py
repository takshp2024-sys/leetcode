class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array to easily find the median
        nums.sort()
        
        # The median is the middle element. 
        # For an even number of elements, either of the two middle elements works.
        median = nums[len(nums) // 2]
        
        # Calculate the total moves required to make all elements equal to the median
        moves = 0
        for num in nums:
            moves += abs(num - median)
            
        return moves