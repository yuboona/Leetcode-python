# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """判断是否为兄弟节点
        1、在遍历过程中保存，x和y的父节点、level两个值
        2、判断层次是否相同，再判断父节点
    """
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_info = []
        y_info = []
        if root == None:
            return False
        if not root.left:
            return False
        if not root.right:
            return False
        # 从0层开始
        level = 0

        def helper(parent_, root_, level_):
            if root_.val == x:
                x_info.append(parent_)
                x_info.append(level_)
            if root_.val == y:
                y_info.append(parent_)
                y_info.append(level_)
            if root_.left:
                helper(root_, root_.left, level_+1)
            if root_.right:
                helper(root_, root_.right, level_+1)
        helper(None, root, level)
        if x_info[1] == y_info[1]:
            if x_info[0] != y_info[0]:
                return True
            else:
                return False
        else:
            return False
