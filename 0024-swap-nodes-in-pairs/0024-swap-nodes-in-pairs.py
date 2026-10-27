# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Create a dummy node to handle edge cases (like swapping the first two nodes)
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' points to the node right before the pair we are going to swap
        prev = dummy
        
        # While there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Perform the swap
            # 1. Point prev to the second node (the new head of this pair)
            prev.next = second
            # 2. Point the first node to what comes after the second node
            first.next = second.next
            # 3. Point the second node to the first node
            second.next = first
            
            # Move 'prev' two steps forward to be ready for the next pair
            prev = first
            
        return dummy.next