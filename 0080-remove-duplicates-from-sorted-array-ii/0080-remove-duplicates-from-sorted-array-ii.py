class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array has 2 or fewer elements, it's already valid
        if len(nums) <= 2:
            return len(nums)
        
        # k is the pointer where the next valid element should be placed.
        # We start at 2 because the first two elements are always valid.
        k = 2
        
        # Iterate through the array starting from index 2
        for i in range(2, len(nums)):
            # If the current element is different from the element at k-2,
            # it means we haven't exceeded the limit of 2 duplicates.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k