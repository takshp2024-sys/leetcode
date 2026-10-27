# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node that points to the head. 
        # This handles edge cases like removing the head node itself.
        dummy = ListNode(0, head)
        
        # Initialize both pointers at the dummy node
        fast = dummy
        slow = dummy
        
        # Move the fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # At this point, slow is right before the node we need to remove
        # Skip the nth node from the end
        slow.next = slow.next.next
        
        # Return the new head
        return dummy.next  