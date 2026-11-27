class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        # Helper function to find the maximum number of length 'l' from a single array
        def max_single_array(nums: List[int], l: int) -> List[int]:
            stack = []
            # We need to drop len(nums) - l elements
            drop = len(nums) - l
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            # Return the first 'l' elements
            return stack[:l]
            
        # Helper function to merge two arrays into the maximum possible array
        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            res = []
            i, j = 0, 0
            while i < len(arr1) or j < len(arr2):
                # Compare the remaining parts of arr1 and arr2
                # If arr1[i:] > arr2[j:], we pick from arr1; otherwise, from arr2
                if arr1[i:] > arr2[j:]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            return res
            
        m, n = len(nums1), len(nums2)
        max_res = []
        
        # Try all possible splits of k between nums1 and nums2
        # i is the number of elements taken from nums1
        for i in range(max(0, k - n), min(k, m) + 1):
            # Get the maximum subarray of length i from nums1
            part1 = max_single_array(nums1, i)
            # Get the maximum subarray of length k-i from nums2
            part2 = max_single_array(nums2, k - i)
            
            # Merge the two parts
            candidate = merge(part1, part2)
            
            # Update the maximum result
            if candidate > max_res:
                max_res = candidate
                
        return max_res