# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def backtrack(node: Optional[TreeNode], current_path: List[int], current_sum: int):
            if not node:
                return
                
            # Add the current node to the path and update the sum
            current_path.append(node.val)
            current_sum += node.val
            
            # Check if it's a leaf node and the sum matches the target
            if not node.left and not node.right and current_sum == targetSum:
                # Append a copy of the current path to the result
                result.append(list(current_path))
            else:
                # Continue exploring the left and right subtrees
                backtrack(node.left, current_path, current_sum)
                backtrack(node.right, current_path, current_sum)
                
            # Backtrack: remove the current node to explore other paths
            current_path.pop()
            
        backtrack(root, [], 0)
        return result