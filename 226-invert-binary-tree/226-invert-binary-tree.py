# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertUtil(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return
            temp = node.right
            node.right = invertUtil(node.left)
            node.left = invertUtil(temp)
            return node
        
        return invertUtil(root)