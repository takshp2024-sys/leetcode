class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_positive_sum = float('inf')
        
        # Iterate through all possible starting indices
        for i in range(n):
            current_sum = 0
            # Iterate through possible ending indices
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                
                # Check if the length is within the valid range [l, r]
                if l <= length <= r:
                    # Check if the sum is positive and smaller than our current minimum
                    if current_sum > 0:
                        min_positive_sum = min(min_positive_sum, current_sum)
                        
                # Optimization: If length exceeds r, we can break early for this starting index
                if length > r:
                    break
                    
        # If we didn't find any valid subarray, return -1
        return min_positive_sum if min_positive_sum != float('inf') else -1