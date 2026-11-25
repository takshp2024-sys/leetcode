class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Double hashing to avoid collisions
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base = 131
        
        # Precompute powers for both moduli
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        for i in range(1, n + 1):
            p1[i] = (p1[i - 1] * base) % mod1
            p2[i] = (p2[i - 1] * base) % mod2
            
        def check(length: int) -> bool:
            if length > n:
                return False
                
            # Compute initial hashes for the first window of size 'length'
            h1 = 0
            h2 = 0
            for i in range(length):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
                
            counts = {}
            counts[(h1, h2)] = 1
            
            # Slide the window
            for i in range(length, n):
                # Remove the leftmost element and add the new element
                h1 = (h1 - nums[i - length] * p1[length - 1]) % mod1
                h1 = (h1 * base + nums[i]) % mod1
                
                h2 = (h2 - nums[i - length] * p2[length - 1]) % mod2
                h2 = (h2 * base + nums[i]) % mod2
                
                key = (h1, h2)
                counts[key] = counts.get(key, 0) + 1
                
            # Check if any hash appears exactly once
            for count in counts.values():
                if count == 1:
                    return True
                    
            return False

        # Binary search for the minimum valid length
        left, right = 1, n
        ans = n
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans