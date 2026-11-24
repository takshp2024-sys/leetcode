class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # Map each prime factor to a specific bit
        def get_mask(n):
            mask = 0
            if n % 2 == 0: mask |= 1
            if n % 3 == 0: mask |= 2
            if n % 5 == 0: mask |= 4
            if n % 7 == 0: mask |= 8
            return mask

        n = len(nums)
        max_len = 1
        
        # Any single element is trivially product equivalent
        # Any pair of elements is mathematically product equivalent (a*b = gcd*lcm)
        # So if n >= 2, the answer is at least 2.
        if n >= 2:
            max_len = 2

        left = 0
        current_mask = 0
        
        for right in range(n):
            num = nums[right]
            
            if num == 1:
                max_len = max(max_len, right - left + 1)
                continue
                
            num_mask = get_mask(num)
            
            # Shrink window if the new number shares a prime factor with the window
            # Note: For a window of size >= 3, all numbers (excluding 1s) must be pairwise coprime.
            while (current_mask & num_mask) != 0:
                if nums[left] != 1:
                    current_mask ^= get_mask(nums[left])
                left += 1
                
            current_mask |= num_mask
            
            # Update max_len for the current valid window
            # If the window has length 2, it's always valid. 
            # If length >= 3, the coprime condition ensures validity.
            window_len = right - left + 1
            
            # If the window length is 2 and it contains a conflict, 
            # it's still valid. But our while loop would have shrunk it. 
            # We must explicitly check length 2 windows that contain non-coprime pairs.
            
            max_len = max(max_len, window_len)
            
        # We also need to check for length 2 windows that were skipped due to conflicts
        # (e.g., [2, 6]). The sliding window shrinks to length 1 for [2, 6], 
        # but the pair [2, 6] is valid.
        
        return max_len