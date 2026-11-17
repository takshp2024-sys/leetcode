class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        # Initialize cost with infinity
        cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        
        for length in range(2, n + 1): # length 1 is not allowed
            for i in range(n - length + 1):
                j = i + length
                substring = s[i:j]
                
                min_ops = float('inf')
                for d in range(1, length):
                    if length % d == 0:
                        ops = 0
                        for offset in range(d):
                            group = [substring[idx] for idx in range(offset, length, d)]
                            l, r = 0, len(group) - 1
                            while l < r:
                                if group[l] != group[r]:
                                    ops += 1
                                l += 1
                                r -= 1
                        min_ops = min(min_ops, ops)
                cost[i][j] = min_ops
        
        # DP
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # We must ensure the last substring has length >= 2
                for p in range(i - 1, -1, -1):
                    if i - p >= 2 and dp[p][j - 1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i])
                        
        return dp[n][k]