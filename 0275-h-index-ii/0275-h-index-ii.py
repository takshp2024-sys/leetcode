class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # The number of papers with at least citations[mid] citations is n - mid
            if citations[mid] == n - mid:
                # We found the exact point
                return n - mid
            elif citations[mid] < n - mid:
                # The number of citations is less than the number of papers remaining.
                # The h-index must be smaller, so we need to look at the right half (more citations).
                left = mid + 1
            else:
                # The number of citations is greater than or equal to the number of papers remaining.
                # We might be able to find a larger h-index, so look left.
                right = mid - 1
                
        # When the loop ends, 'left' will be the first index where citations[i] >= n - i.
        # The h-index is the number of papers from index 'left' to the end.
        return n - left