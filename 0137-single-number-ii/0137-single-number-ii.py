class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize variables to track the bits that have appeared once and twice
        ones = 0
        twos = 0
        
        for num in nums:
            # Update 'twos' and 'ones' using bitwise operations
            # 'twos' tracks bits that have appeared twice
            # 'ones' tracks bits that have appeared once
            twos = twos ^ (ones & num)
            ones = ones ^ num
            
            # If a bit has appeared three times, it will be in both 'ones' and 'twos'
            # We clear it from both using a mask
            mask = ~(ones & twos)
            ones &= mask
            twos &= mask
            
        # The unique number is stored in 'ones'
        return ones