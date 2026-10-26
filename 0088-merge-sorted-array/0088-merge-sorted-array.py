class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for the end of the meaningful elements in nums1, 
        # the end of nums2, and the very end of nums1 (where we will insert)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # While there are elements to process in both arrays
        while p1 >= 0 and p2 >= 0:
            # Compare the largest available elements from the end of each array
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            # Move the insertion pointer forward
            p -= 1
            
        # If there are remaining elements in nums2, copy them over.
        # (If there are remaining elements in nums1, they are already in the correct place!)
        nums1[:p2 + 1] = nums2[:p2 + 1]