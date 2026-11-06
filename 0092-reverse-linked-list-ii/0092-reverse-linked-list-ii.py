# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: if there's nothing to reverse
        if not head or left == right:
            return head
            
        # Create a dummy node to handle the edge case where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 1. Move 'prev' to the node right before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
            
        # 'prev' is now the node before the sublist.
        # 'current' is the first node of the sublist to be reversed.
        current = prev.next
        
        # 2. Reverse the sublist using the Head Insertion technique
        # We need to perform (right - left) insertions
        for _ in range(right - left):
            # 'next_node' is the node we want to move to the front of the sublist
            next_node = current.next
            
            # Remove 'next_node' from its current position
            current.next = next_node.next
            
            # Insert 'next_node' right after 'prev'
            next_node.next = prev.next
            prev.next = next_node
            
        return dummy.next