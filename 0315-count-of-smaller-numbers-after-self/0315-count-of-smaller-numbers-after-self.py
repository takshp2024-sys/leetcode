class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Coordinate Compression
        sorted_unique = sorted(list(set(nums)))
        # Map each value to its rank (1-indexed)
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        m = len(sorted_unique)
        
        # Fenwick Tree
        tree = [0] * (m + 1)
        
        def update(index: int) -> None:
            while index <= m:
                tree[index] += 1
                index += index & (-index)
                
        def query(index: int) -> int:
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & (-index)
            return total
            
        n = len(nums)
        result = [0] * n
        
        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            rank = rank_map[nums[i]]
            # Count elements strictly smaller, which corresponds to query(rank - 1)
            result[i] = query(rank - 1)
            # Add the current element to the Fenwick Tree
            update(rank)
            
        return result