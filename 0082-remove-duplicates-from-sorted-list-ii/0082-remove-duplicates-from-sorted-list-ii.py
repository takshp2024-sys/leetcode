# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node pointing to the head to handle edge cases
        # where the first few nodes are duplicates.
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # If we find duplicates, skip all nodes with the same value
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip the last duplicate node
                prev.next = head.next
            else:
                # If no duplicates, just move the 'prev' pointer forward
                prev = prev.next
                
            # Move the 'head' pointer forward
            head = head.next
            
        return dummy.next