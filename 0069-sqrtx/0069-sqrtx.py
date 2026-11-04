class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 1, x // 2
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                # mid is a valid candidate, but we might find a larger one
                result = mid
                left = mid + 1
            else:
                # mid is too large, search the left half
                right = mid - 1
                
        return result