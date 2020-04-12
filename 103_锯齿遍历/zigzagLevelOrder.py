# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """迭代方法
            level迭代遍历不变，在插入值时，根据输出方向的不同，进行头或尾的插入
        """
        if not root:
            return []
        Q = deque()
        Q.append(root)
        level = 0
        levels = []
        while  len(Q) > 0:
            temp = []
            level_len = len(Q)
            for i in range(level_len):
                node = Q.popleft()
                if level%2 == 0:
                    temp.append(node.val)
                    if node.left:
                        Q.append(node.left)
                    if node.right:
                        Q.append(node.right)
                if level%2 == 1:
                    temp.insert(0, node.val)
                    if node.left:
                        Q.append(node.left)
                    if node.right:
                        Q.append(node.right)
            levels.append(temp)
        return levels
