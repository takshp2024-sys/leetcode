# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Initialize the heap
        min_heap = []
        
        # Push the head of each non-empty linked list into the heap.
        # We use a counter 'i' to break ties if two nodes have the same value,
        # because Python's heapq cannot compare ListNode objects directly.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
                
        # Dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        
        # Extract the minimum node from the heap until it's empty
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Add the smallest node to our merged list
            current.next = node
            current = current.next
            
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        # Return the head of the merged list
        return dummy.next