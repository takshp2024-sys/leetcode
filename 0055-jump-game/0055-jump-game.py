class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # max_reach keeps track of the furthest index we can reach so far
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # If the current index is greater than the furthest we can reach, 
            # it means there's a gap we can't cross, so we can't reach the end.
            if i > max_reach:
                return False
            
            # Update the furthest index we can reach from the current position
            max_reach = max(max_reach, i + jump)
            
            # Optimization: If we can already reach the last index, we can stop early
            if max_reach >= len(nums) - 1:
                return True
                
        return True