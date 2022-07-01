# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root :
            return []
        
        def DFS(node, targetSum,road) :
            if node.left== None and node.right==None and targetSum==node.val :
                road +=[node.val]
                roads.append(road)
                return 
            if node.left or node.right :
                if node.left :
                    DFS(node.left, targetSum-node.val,road+[node.val])
                if node.right:
                    DFS(node.right, targetSum-node.val,road+[node.val])
        roads = []
        DFS(root,targetSum,[])
        return roads
        