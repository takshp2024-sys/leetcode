# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: If the left pointer exceeds the right, there are no elements to form a tree
            if left > right:
                return None
                
            # Find the middle index
            mid = (left + right) // 2
            
            # The middle element becomes the root
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        return build(0, len(nums) - 1)