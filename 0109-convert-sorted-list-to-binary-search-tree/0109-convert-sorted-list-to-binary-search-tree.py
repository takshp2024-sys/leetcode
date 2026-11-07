# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 1: Count the total number of nodes in the linked list
        current = head
        size = 0
        while current:
            size += 1
            current = current.next
            
        # Keep a reference to the head to advance through the list during recursion
        self.node = head
        
        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no nodes to process
            if left > right:
                return None
                
            mid = (left + right) // 2
            
            # Recursively build the left subtree
            left_child = build_tree(left, mid - 1)
            
            # The current node in the linked list is the root of this subtree
            root = TreeNode(self.node.val)
            root.left = left_child
            
            # Advance the linked list pointer
            self.node = self.node.next
            
            # Recursively build the right subtree
            root.right = build_tree(mid + 1, right)
            
            return root
            
        return build_tree(0, size - 1)