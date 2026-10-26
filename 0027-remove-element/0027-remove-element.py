class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next valid position
        
        for i in range(len(nums)):
            # If the current element is not the value to remove
            if nums[i] != val:
                # Place it at the next valid position
                nums[k] = nums[i]
                k += 1
                
        return k