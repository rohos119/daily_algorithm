# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 문제정의 : BST를 출력해라
# input : 1 nums 1e4
# output : [root, root.left,root.right] // if left or right 없을땐 null도 가능
class Solution:
    def formNodes(self,nums, l,r):
        if l > r:
            return None
        else:
            mid = l+(r-l)//2
            node = TreeNode(nums[mid])
            node.left = self.formNodes(nums, l,mid-1)
            node.right = self.formNodes(nums, mid+1,r)
            return node
        
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.formNodes(nums, 0,len(nums)-1)
        