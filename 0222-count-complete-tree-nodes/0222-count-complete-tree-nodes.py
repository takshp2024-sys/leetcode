# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # Function to calculate the height of the tree (or subtree)
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
            
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        if left_height == right_height:
            # If left and right heights are equal, the left subtree is a perfect tree.
            # Total nodes = nodes in perfect left subtree + 1 (root) + nodes in right subtree.
            # A perfect tree of height h has 2^h - 1 nodes.
            return (1 << left_height) - 1 + 1 + self.countNodes(root.right)
        else:
            # If heights are not equal, the right subtree is a perfect tree.
            # Total nodes = nodes in left subtree + 1 (root) + nodes in perfect right subtree.
            return (1 << right_height) - 1 + 1 + self.countNodes(root.left)