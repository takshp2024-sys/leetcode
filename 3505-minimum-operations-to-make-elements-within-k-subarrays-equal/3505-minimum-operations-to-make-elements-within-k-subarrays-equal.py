import bisect

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # 1. Coordinate Compression
        # Get unique sorted values to map them to indices 1..M
        unique_vals = sorted(list(set(nums)))
        M = len(unique_vals)
        
        # Map value to its compressed index (1-based for Fenwick tree)
        val_to_idx = {v: i + 1 for i, v in enumerate(unique_vals)}
        
        # Fenwick Tree for counts and sums
        bit_count = [0] * (M + 1)
        bit_sum = [0] * (M + 1)
        
        def add(idx, delta_count, delta_sum):
            while idx <= M:
                bit_count[idx] += delta_count
                bit_sum[idx] += delta_sum
                idx += idx & (-idx)
                
        def query(idx):
            c = 0
            s = 0
            while idx > 0:
                c += bit_count[idx]
                s += bit_sum[idx]
                idx -= idx & (-idx)
            return c, s
            
        def find_kth(k):
            # Find the smallest index such that the prefix sum of counts >= k
            idx = 0
            bit_mask = 1 << (M.bit_length())
            while bit_mask:
                t = idx + bit_mask
                if t <= M and bit_count[t] < k:
                    idx = t
                    k -= bit_count[t]
                bit_mask >>= 1
            return idx + 1
            
        cost = [0] * (n - x + 1)
        
        # Initialize the first window
        for i in range(x):
            idx = val_to_idx[nums[i]]
            add(idx, 1, nums[i])
            
        # The median is the (x + 1) // 2 -th smallest element
        median_rank = (x + 1) // 2
        
        for i in range(n - x + 1):
            # Find median index
            med_idx = find_kth(median_rank)
            median_val = unique_vals[med_idx - 1]
            
            # Calculate cost to make all elements equal to median
            c_left, s_left = query(med_idx) # Includes the median
            c_right, s_right = query(M)
            
            c_right -= c_left
            s_right -= s_left
            
            # Cost = (median * count_left - sum_left) + (sum_right - median * count_right)
            cost[i] = (median_val * c_left - s_left) + (s_right - median_val * c_right)
            
            # Slide the window: remove nums[i], add nums[i + x]
            if i + x < n:
                out_idx = val_to_idx[nums[i]]
                add(out_idx, -1, -nums[i])
                
                in_idx = val_to_idx[nums[i + x]]
                add(in_idx, 1, nums[i + x])
                
        # 2. Dynamic Programming
        INF = float('inf')
        m_len = len(cost)
        
        dp = [INF] * m_len
        for i in range(m_len):
            if i == 0:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i - 1], cost[i])
                
        if k == 1:
            return dp[-1]
            
        for m in range(2, k + 1):
            new_dp = [INF] * m_len
            min_prev = INF
            
            for i in range(m_len):
                if i - x >= 0:
                    min_prev = min(min_prev, dp[i - x])
                    
                if min_prev != INF:
                    new_dp[i] = min_prev + cost[i]
                    
            for i in range(1, m_len):
                new_dp[i] = min(new_dp[i], new_dp[i - 1])
                
            dp = new_dp
            
        return dp[-1]