# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
            
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now at the middle. The second half starts after 'slow'
        second_half = slow.next
        slow.next = None  # Break the link to separate the two halves
        
        # Step 2: Reverse the second half
        prev = None
        current = second_half
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
            
        # 'prev' is now the head of the reversed second half
        second_half = prev
        
        # Step 3: Merge the two halves
        first_half = head
        while second_half:
            # Save the next nodes
            temp1 = first_half.next
            temp2 = second_half.next
            
            # Link first_half to second_half
            first_half.next = second_half
            # Link second_half to the next node in the first half
            second_half.next = temp1
            
            # Advance the pointers
            first_half = temp1
            second_half = temp2