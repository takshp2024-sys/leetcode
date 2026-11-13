class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Reverse the array for easier right-to-left processing
        nums = nums[::-1]
        
        # Stack to maintain the blocks of values
        # Each element is a tuple: (value, count)
        stack = []
        ans = 0
        left = 0
        curr_cost = 0
        
        for right in range(n):
            # Add the new element as a new block
            count = 1
            while stack and stack[-1][0] < nums[right]:
                val, cnt = stack.pop()
                # Merge the block
                curr_cost += (nums[right] - val) * cnt
                count += cnt
            stack.append((nums[right], count))
            
            # Shrink the window if the cost exceeds k
            while curr_cost > k:
                # We need to remove the leftmost element from the window
                # The leftmost element is at the bottom of the stack (index 0)
                val, cnt = stack[0]
                
                if cnt == 1:
                    # Remove the block entirely
                    stack.pop(0)
                else:
                    # Reduce the count of the first block
                    stack[0] = (val, cnt - 1)
                
                # Update curr_cost: The cost contributed by the leftmost element is
                # (the value it was raised to - its original value).
                # The value it was raised to is the value of the block it belongs to.
                # But we need to know the original value. Since we reversed, the original is nums[left].
                # However, it might have been raised to a higher value.
                # The block it belongs to has value 'val'. The original is nums[left].
                # So the cost reduction is (val - nums[left]).
                curr_cost -= (val - nums[left])
                
                left += 1
                
            # All subarrays ending at 'right' starting from 'left' to 'right' are valid
            ans += (right - left + 1)
            
        return ans