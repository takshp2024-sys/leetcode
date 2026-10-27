class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the candidate and a counter
        candidate = None
        count = 0
        
        # First pass: Find the majority candidate
        for num in nums:
            if count == 0:
                # If count drops to 0, we pick a new candidate
                candidate = num
            
            # If we see the candidate, increment count; otherwise, decrement
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate