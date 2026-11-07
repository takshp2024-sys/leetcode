# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map inorder values to their indices for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Start processing postorder from the end
        post_idx = len(postorder) - 1
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_idx
            
            # Base case: no elements to construct the tree
            if left > right:
                return None
                
            # The current root is the last element in the remaining postorder
            root_val = postorder[post_idx]
            post_idx -= 1
            
            root = TreeNode(root_val)
            
            # Find the root's index in inorder to split left and right subtrees
            mid = inorder_map[root_val]
            
            # Important: Build the right subtree first!
            # Because we are traversing postorder backwards (Root -> Right -> Left)
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            
            return root
            
        return build(0, len(inorder) - 1)