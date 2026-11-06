# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
            
        # Memoization dictionary to store the results of subproblems
        memo = {}
        
        def build_trees(start: int, end: int) -> List[TreeNode]:
            # Base case: if start > end, there are no numbers left, return [None]
            if start > end:
                return [None]
                
            # Check if the result is already in memo
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            
            # Pick a root for the current range
            for i in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)
                
                # Combine left and right subtrees with the current root
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            # Save the result in memo before returning
            memo[(start, end)] = all_trees
            return all_trees
            
        return build_trees(1, n)