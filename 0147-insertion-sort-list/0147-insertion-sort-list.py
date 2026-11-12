# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the sorted list
        dummy = ListNode(0)
        current = head
        
        while current:
            # Save the next node before modifying pointers
            next_node = current.next
            
            # Start from the beginning of the sorted list
            prev = dummy
            
            # Find the correct insertion point (first node with value >= current.val)
            while prev.next and prev.next.val < current.val:
                prev = prev.next
                
            # Insert the current node after 'prev'
            current.next = prev.next
            prev.next = current
            
            # Move to the next node in the original list
            current = next_node
            
        return dummy.next