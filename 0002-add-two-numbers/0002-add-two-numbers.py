# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to easily build the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop as long as there are nodes to process or a carry remains
        while l1 or l2 or carry:
            # Get the values of the current nodes (0 if the list has ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum for the current position
            total = val1 + val2 + carry
            
            # Update carry for the next position
            carry = total // 10
            
            # The digit to store is the remainder
            current.next = ListNode(total % 10)
            
            # Move to the next nodes
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # Return the result list, skipping the dummy head
        return dummy.next