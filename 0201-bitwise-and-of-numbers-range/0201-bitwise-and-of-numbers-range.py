class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        
        # Find the common prefix by shifting both numbers right until they are equal
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
            
        # Shift the common prefix back to the left to get the final result
        return left << shift