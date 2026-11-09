"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
            
        # 'current' acts as the head of the current level being processed
        current = root
        
        while current:
            # Dummy node to act as the start of the next level's linked list
            dummy = Node(0)
            # 'tail' keeps track of the last node added to the next level
            tail = dummy
            
            # Traverse the current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                    
                # Move to the next node in the current level
                current = current.next
                
            # Move to the start of the next level
            current = dummy.next
            
        return root