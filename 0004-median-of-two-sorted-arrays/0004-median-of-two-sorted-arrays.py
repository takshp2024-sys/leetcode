class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to guarantee O(log(min(m, n))) time
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = total_len // 2
        
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2
            # Partition nums2 such that left side has exactly half_len elements
            partition2 = half_len - partition1
            
            # Find the max of the left side and min of the right side
            # Use -inf and +inf for edge cases where partitions are at the boundaries
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            min_right1 = nums1[partition1] if partition1 < m else float('inf')
            
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            min_right2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is odd, the median is the min of the right side
                if total_len % 2 == 1:
                    return min(min_right1, min_right2)
                # If total length is even, the median is the average of max left and min right
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            
            # If nums1's left side is too big, move the partition left
            elif max_left1 > min_right2:
                right = partition1 - 1
            # If nums2's left side is too big, move the partition right
            else:
                left = partition1 + 1