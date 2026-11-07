# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a map to find the index of any value in inorder in O(1) time
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Use an iterator for preorder to easily get the next root
        preorder_iter = iter(preorder)
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: If the left boundary exceeds the right, there are no elements to construct
            if left > right:
                return None
                
            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find the position of the root in the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        return build(0, len(inorder) - 1)