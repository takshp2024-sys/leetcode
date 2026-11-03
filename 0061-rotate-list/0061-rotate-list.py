# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find the length of the list and the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Calculate the effective rotation
        # If k is greater than length, we only need to rotate k % length times
        k = k % length
        if k == 0:
            return head
            
        # 3. Form a circular linked list by connecting the tail to the head
        tail.next = head
        
        # 4. Find the new tail and new head
        # The new tail will be at position (length - k - 1) from the start
        # The new head will be the node right after the new tail
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # 5. Break the ring
        new_tail.next = None
        
        return new_head