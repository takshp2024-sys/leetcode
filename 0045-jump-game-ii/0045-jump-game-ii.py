class Solution:
    def jump(self, nums: list[int]) -> int:
        # If the array has only 1 element, we are already at the last index
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # We don't need to process the last element because we've already reached it
        # when our farthest >= len(nums) - 1
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from the current position
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the range for the current jump,
            # we MUST make another jump to go further.
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
                # If the new range reaches or exceeds the last index, we are done
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps
