# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes to act as the heads of the two new lists
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to build the two lists
        less_tail = less_dummy
        greater_tail = greater_dummy
        
        current = head
        
        # Traverse the original list
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
                
            current = current.next
            
        # Important: Set the next of the last node in the greater list to None
        # to prevent a cycle or connecting back to a node from the original list.
        greater_tail.next = None
        
        # Connect the end of the less list to the start of the greater list
        less_tail.next = greater_dummy.next
        
        # The head of the new partitioned list is the start of the less list
        return less_dummy.next