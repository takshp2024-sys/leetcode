# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.index = 0
#
#     def hasNext(self) -> bool:
#         return self.index < len(self.nums)
#
#     def next(self) -> int:
#         val = self.nums[self.index]
#         self.index += 1
#         return val

class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self.next_val = None  # Cache for the peeked element
        self.has_cached = False

    def peek(self) -> int:
        # If we haven't cached the next value yet, fetch it
        if not self.has_cached:
            self.next_val = self.iterator.next()
            self.has_cached = True
        return self.next_val

    def next(self) -> int:
        # If we have a cached value, return it and clear the cache
        if self.has_cached:
            self.has_cached = False
            return self.next_val
        # Otherwise, fetch the next value directly from the iterator
        return self.iterator.next()

    def hasNext(self) -> bool:
        # There are more elements if we have a cached value or the iterator has more
        return self.has_cached or self.iterator.hasNext()