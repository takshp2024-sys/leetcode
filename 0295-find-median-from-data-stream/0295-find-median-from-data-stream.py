import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap for the smaller half (store negatives to simulate max-heap)
        self.small = []
        # Min-heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to the max-heap (smaller half)
        heapq.heappush(self.small, -num)
        
        # Ensure the largest element in 'small' is <= the smallest element in 'large'
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance the sizes: 'small' can have at most 1 more element than 'large'
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # Odd number of elements: median is the top of the max-heap
            return float(-self.small[0])
        else:
            # Even number of elements: median is the average of the two tops
            return (-self.small[0] + self.large[0]) / 2.0