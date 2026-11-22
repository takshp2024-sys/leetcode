# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
            
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now at the middle. The second half starts after 'slow'
        second_half_start = slow.next
        
        # Step 2: Reverse the second half
        prev = None
        current = second_half_start
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
            
        # 'prev' is the head of the reversed second half
        reversed_second_half = prev
        
        # Step 3: Compare the first half and the reversed second half
        first_half = head
        second_half = reversed_second_half
        
        # Compare nodes
        is_palindrome = True
        while second_half:
            if first_half.val != second_half.val:
                is_palindrome = False
                break
            first_half = first_half.next
            second_half = second_half.next
            
        # Optional: Restore the original list (Good practice)
        # Reverse the second half back
        prev = None
        current = reversed_second_half
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        slow.next = prev
        
        return is_palindrome