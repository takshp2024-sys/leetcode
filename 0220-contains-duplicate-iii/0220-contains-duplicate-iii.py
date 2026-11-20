class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
            
        # Dictionary to store the buckets: bucket_id -> num
        buckets = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
            # Get the bucket ID for the current number
            bucket_id = num // bucket_size
            
            # 1. Check if the current bucket already has a number
            if bucket_id in buckets:
                return True
                
            # 2. Check the adjacent left bucket
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # 3. Check the adjacent right bucket
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
                
            # Add the current number to its bucket
            buckets[bucket_id] = num
            
            # Maintain the sliding window of size indexDiff
            if i >= indexDiff:
                # Remove the element that is sliding out of the window
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]
                
        return False