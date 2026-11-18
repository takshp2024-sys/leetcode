# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # Skip the node with the matching value
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
                
        return dummy.next