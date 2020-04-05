# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

set.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        迭代方法
        """
        if not root:
            return []
        Q = deque()
        Q.append(root)
        res = []
        while len(Q) > 0:

            level_length = len(Q)
            temp = []
            for i in range(level_length):
                now = Q.popleft()
                temp.append(now.val)
                if now.left:
                    Q.append(now.left)
                if now.right:
                    Q.append(now.right)
                
            res.append(temp)

        return res

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     """
    #     递归方法
    #     """
    #     res = []
    #     level = 0
    #     if root == None:
    #             return []
    #     def helper(root: TreeNode, level: int):
    #         """
    #         # 闭包函数可以不用传递res: List[List[int]]
    #         """
    #         if len(res) == level:
    #             # 因为每一层，这句话不只访问一次
    #             # 要在第一次访问时加入新的[]
    #             res.append([])
    #         res[level].append(root.val)
    #         if root.left:
    #             helper(root.left, level+1)
    #         if root.right:
    #             helper(root.right, level+1)
    #     helper(root, 0)
    #     return res