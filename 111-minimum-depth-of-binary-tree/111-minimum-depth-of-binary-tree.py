# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# start 1705 goal 15m
# 문제정의 : 루트노드에서 자식이 없는 가장 짧은 depth를 구하라
# input : 1 node 1e5
# output : minimum depth -> int
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # print(root.left.val, root.right.val)
        que = deque([[root,0]])
        
        if root == None :
            return 0
        
        depth = 1
        while True :
            n_node,depth = que.popleft()
            depth += 1
            #print(n_node)
            if n_node.left == None and n_node.right == None :
                return depth
            
            if n_node.left :
                que.append([n_node.left,depth])
            if n_node.right :
                que.append([n_node.right,depth])
            #print(que, n_node)