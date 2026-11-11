"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Step 1: Create a copy of each node and insert it right after the original node.
        # Original: A -> B -> C
        # Weaved:   A -> A' -> B -> B' -> C -> C'
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next
            
        # Step 2: Assign the 'random' pointers for the copied nodes.
        current = head
        while current:
            if current.random:
                # The copy of the random node is exactly at current.random.next
                current.next.random = current.random.next
            current = current.next.next
            
        # Step 3: Separate the weaved list into the original list and the copied list.
        current = head
        copy_head = head.next
        
        while current:
            copy_node = current.next
            # Restore the original list's next pointer
            current.next = copy_node.next
            # Set the copied list's next pointer
            if copy_node.next:
                copy_node.next = copy_node.next.next
            # Move to the next original node
            current = current.next
            
        return copy_head