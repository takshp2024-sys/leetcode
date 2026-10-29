# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # Dummy node to handle edge cases and act as the pre-node for the first group
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Find the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                # If we reach the end of the list before finding k nodes, we are done
                if not kth:
                    return dummy.next
                    
            # The next group's previous node will be the current group's first node
            group_next = kth.next
            
            # Reverse the group
            prev = kth.next
            curr = group_prev.next
            
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # Connect the previous part of the list to the newly reversed group
            temp = group_prev.next  # This is now the last node of the reversed group
            group_prev.next = kth   # group_prev now points to the new head (kth)
            group_prev = temp       # Move group_prev to the end of the reversed group