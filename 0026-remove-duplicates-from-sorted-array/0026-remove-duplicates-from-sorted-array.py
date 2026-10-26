class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array is empty, there are 0 unique elements
        if not nums:
            return 0
            
        # k represents the index where the next unique element should be placed.
        # Since the first element is always unique, we start k at 1.
        k = 1
        
        # Iterate through the array with pointer i (starting from the second element)
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # it's a new unique element.
            if nums[i] != nums[i - 1]:
                # Place the unique element at the k-th position
                nums[k] = nums[i]
                # Move the k pointer forward
                k += 1
                
        # k is exactly the number of unique elements
        return k