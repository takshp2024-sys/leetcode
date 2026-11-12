# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        # Step 1: Count the total number of nodes
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        # Dummy node to easily handle the new head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 2: Iteratively merge sublists of size 'step' (1, 2, 4, 8...)
        step = 1
        while step < length:
            prev = dummy
            curr = dummy.next
            
            while curr:
                # Split the list into two halves: left and right
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step) # 'curr' is the start of the next pair
                
                # Merge the two halves and attach to the previous sorted part
                prev = self.merge(left, right, prev)
                
            step *= 2
            
        return dummy.next
        
    def split(self, head: ListNode, step: int) -> Optional[ListNode]:
        """Splits the list after 'step' nodes and returns the head of the second half."""
        if not head:
            return None
            
        current = head
        # Move 'step - 1' times to find the tail of the first half
        for _ in range(step - 1):
            if not current.next:
                break
            current = current.next
            
        second_half = current.next
        current.next = None  # Break the link
        return second_half
        
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode], prev: ListNode) -> ListNode:
        """Merges two sorted lists and attaches the result after 'prev'."""
        current = prev
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        # Attach the remaining nodes
        current.next = l1 if l1 else l2
        
        # Advance current to the tail of the merged list
        while current.next:
            current = current.next
            
        return current