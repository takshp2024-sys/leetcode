# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
        
    def _push_left(self, node: Optional[TreeNode]):
        # Push all left children onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top of the stack is the next smallest element
        node = self.stack.pop()
        
        # If the node has a right child, push all its left children
        if node.right:
            self._push_left(node.right)
            
        return node.val

    def hasNext(self) -> bool:
        # If the stack is not empty, there are more elements
        return len(self.stack) > 0