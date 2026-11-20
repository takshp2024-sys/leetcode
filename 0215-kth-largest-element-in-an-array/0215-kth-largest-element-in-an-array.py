import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty min-heap
        heap = []
        
        # Iterate through the array
        for num in nums:
            heapq.heappush(heap, num)
            # Keep the heap size at most k
            if len(heap) > k:
                heapq.heappop(heap)
                
        # The top of the heap is the kth largest element
        return heap[0]