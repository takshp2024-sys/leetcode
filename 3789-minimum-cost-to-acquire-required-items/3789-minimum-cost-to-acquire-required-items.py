class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # We will check a few candidate numbers of 'both' items.
        # The optimal number of both items will be at one of the boundaries:
        # 0, need1, need2, or min(need1, need2).
        # We can also just check b from 0 to min(need1, need2) if the range is small,
        # but since it can be 10^9, we only check the boundaries.
        
        candidates = {0, need1, need2, min(need1, need2)}
        
        ans = float('inf')
        
        for b in candidates:
            # If we use b items of type 3, we cover b units of type 1 and b units of type 2.
            # Remaining requirements:
            rem1 = max(0, need1 - b)
            rem2 = max(0, need2 - b)
            
            # We can cover the remaining requirements with type 1 and type 2 items.
            # But wait, we could also use MORE type 3 items to cover the remaining requirements if it's cheaper.
            # Actually, the candidate b already includes b = need1 or b = need2, which covers using extra type 3 items.
            # Let's just calculate the cost for this b, assuming we use type 1 and 2 for the rest.
            
            cost = b * costBoth + rem1 * cost1 + rem2 * cost2
            ans = min(ans, cost)
            
        return ans