class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # 1. Sort logs based on time
        logs.sort(key=lambda log: log[1])
        
        # 2. Sort queries while keeping track of their original indices
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        # 3. Sliding window to find active servers for each query
        # We will count how many UNIQUE servers are present in the current window [query - x, query]
        from collections import defaultdict
        
        active_servers = defaultdict(int)
        active_count = 0  # Number of unique servers currently in the window
        
        left = 0
        right = 0
        m = len(logs)
        ans = [0] * len(queries)
        
        for q, original_idx in sorted_queries:
            # Expand the right pointer to include all logs with time <= q
            while right < m and logs[right][1] <= q:
                server_id = logs[right][0]
                if active_servers[server_id] == 0:
                    active_count += 1
                active_servers[server_id] += 1
                right += 1
                
            # Shrink the left pointer to exclude logs with time < q - x
            while left < m and logs[left][1] < q - x:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    active_count -= 1
                left += 1
                
            # The number of servers with no requests is total servers - active unique servers
            ans[original_idx] = n - active_count
            
        return ans