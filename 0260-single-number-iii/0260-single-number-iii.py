class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get unique1 ^ unique2
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        # Step 2: Isolate the rightmost set bit (where unique1 and unique2 differ)
        # In Python, negative numbers are represented with an infinite sequence of leading 1s,
        # so we use a mask to keep it within 32-bit bounds if necessary.
        diff_bit = xor_all & -xor_all
        
        # Step 3: Partition numbers into two groups and XOR them
        unique1 = 0
        unique2 = 0
        
        for num in nums:
            if num & diff_bit:
                unique1 ^= num
            else:
                unique2 ^= num
                
        return [unique1, unique2]