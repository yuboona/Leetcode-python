# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        可以类似看作动态规划，自底向上，每个节点只有两件事需要考虑，
        （1）ans 计算是子树和最大?还是当前root加所有节点的值最大。
        （2）return 左节点或右节点中，和root加起来最长的那条单链
        """

        def dp()