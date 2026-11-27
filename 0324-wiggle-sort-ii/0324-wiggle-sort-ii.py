class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # The smaller half has (n + 1) // 2 elements, the larger has n // 2
        small = sorted_nums[:(n + 1) // 2]
        large = sorted_nums[(n + 1) // 2:]
        
        # Interleave from the end of 'small' and 'large'
        # Odd indices get the largest elements from 'large'
        nums[1::2] = large[::-1]
        # Even indices get the largest elements from 'small'
        nums[0::2] = small[::-1]