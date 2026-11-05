# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # Traverse the list until the second-to-last node
        while current and current.next:
            # If the current node and the next node have the same value,
            # skip the next node by pointing to the node after it.
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # If no duplicate, move to the next node
                current = current.next
                
        return head