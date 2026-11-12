class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
            
        min_val = min(nums)
        max_val = max(nums)
        
        # If all elements are the same, the gap is 0
        if min_val == max_val:
            return 0
            
        n = len(nums)
        # Calculate the minimum possible gap (bucket size)
        # We use integer division and add 1 to ensure the bucket can hold the max value
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        
        # Number of buckets needed
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Initialize buckets to store the min and max values in each bucket
        # We use None to represent empty buckets
        buckets_min = [float('inf')] * bucket_count
        buckets_max = [float('-inf')] * bucket_count
        
        # Place each number into its corresponding bucket
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
            
        max_gap = 0
        prev_max = min_val
        
        # Iterate through the buckets to find the maximum gap
        for i in range(bucket_count):
            # Skip empty buckets
            if buckets_min[i] == float('inf'):
                continue
                
            # The gap is the difference between the current bucket's min and the previous bucket's max
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            # Update prev_max to the current bucket's max
            prev_max = buckets_max[i]
            
        return max_gap