class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        result = []
        start = nums[0]
        
        # We append a dummy value to the end of nums to force the last range to close
        # The dummy value is chosen to not be consecutive to the last element
        nums.append(float('inf'))
        
        for i in range(1, len(nums)):
            # If the current number is not consecutive to the previous one
            if nums[i] != nums[i-1] + 1:
                # If the range has only one number
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i-1]}")
                # Start a new range
                start = nums[i]
                
        return result