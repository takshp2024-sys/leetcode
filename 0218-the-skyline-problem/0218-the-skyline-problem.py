import heapq
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events: (x, height)
        # For start of building, use negative height to distinguish from end in sorting (start comes before end if same x)
        # For end of building, use positive height
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))
            
        # Sort events by x, then by height
        # For the same x:
        # - Start events (negative height) are processed first (highest first)
        # - End events (positive height) are processed last (lowest first)
        # This ensures that if a building ends where another starts at the same height, we don't output a redundant point.
        events.sort()
        
        # Max-heap for active heights (store negatives for max-heap behavior)
        # Start with ground level 0
        max_heap = [0]
        
        # Dictionary to track heights we need to remove from the heap
        to_remove = defaultdict(int)
        
        result = []
        prev_max_height = 0
        
        for x, h in events:
            if h < 0:
                # Start of a building: add height to heap
                heapq.heappush(max_heap, h)
            else:
                # End of a building: mark height for removal
                to_remove[h] += 1
                
            # Lazy deletion: remove heights that are no longer active
            # We check if the top of the heap is marked for removal
            while max_heap and to_remove[-max_heap[0]] > 0:
                to_remove[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
                
            # Get the current maximum height
            current_max_height = -max_heap[0]
            
            # If the maximum height has changed, we have a new key point
            if current_max_height != prev_max_height:
                result.append([x, current_max_height])
                prev_max_height = current_max_height
                
        return result