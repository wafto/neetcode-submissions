# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return 1 + max(depth(node.left), depth(node.right))

        return depth(root)
            