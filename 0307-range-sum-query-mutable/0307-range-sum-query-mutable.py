class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        # Initialize Fenwick Tree (1-indexed)
        self.tree = [0] * (self.n + 1)
        for i, val in enumerate(nums):
            self._add(i + 1, val)

    def _add(self, index: int, delta: int) -> None:
        # Add 'delta' to the element at 'index' in the Fenwick Tree
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)

    def _query(self, index: int) -> int:
        # Calculate the prefix sum up to 'index'
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total

    def update(self, index: int, val: int) -> None:
        # Calculate the difference between the new value and the old value
        delta = val - self.nums[index]
        # Update the original array
        self.nums[index] = val
        # Update the Fenwick Tree with the delta
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        # The sum of a range [left, right] is prefix_sum(right) - prefix_sum(left - 1)
        return self._query(right + 1) - self._query(left)