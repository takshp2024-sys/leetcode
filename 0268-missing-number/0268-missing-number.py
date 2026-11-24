class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        
        for i, num in enumerate(nums):
            # XOR the index, the value, and the current missing result
            missing ^= i ^ num
            
        return missing