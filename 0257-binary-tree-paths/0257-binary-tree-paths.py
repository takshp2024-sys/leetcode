# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
            
        result = []
        
        def dfs(node, current_path):
            # Append the current node's value to the path
            current_path.append(str(node.val))
            
            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                result.append("->".join(current_path))
            else:
                # Otherwise, continue exploring the left and right subtrees
                if node.left:
                    dfs(node.left, current_path)
                if node.right:
                    dfs(node.right, current_path)
                    
            # Backtrack: remove the current node to explore other paths
            current_path.pop()
            
        dfs(root, [])
        return result