import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Sort arr2 to enable binary search
        arr2.sort()
        count = 0
        
        for x in arr1:
            # We want to find if any element in arr2 falls within the range [x - d, x + d]
            # We can use binary search to find the insertion point for (x - d)
            idx = bisect.bisect_left(arr2, x - d)
            
            # If idx is out of bounds, or the closest element at idx is strictly greater than (x + d),
            # then no element in arr2 is within distance d of x.
            if idx == len(arr2) or arr2[idx] > x + d:
                count += 1
                
        return count