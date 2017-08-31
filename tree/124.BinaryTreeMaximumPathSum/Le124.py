#!/usr/bin/env python
# coding=utf-8
#解题思路
#使用一个全局变量current_max，记录当前计算得出的最大路径。递归的思路：左子树中的最大路径和，右子树中的最大路径和，
#以及左子树中以root.left为起点的最大路径（需要大于零）+右子树中以root.right为起点的最大路径（需要大于零）+root.val），
#这三者中的最大值就是最大的路径和
class Solution(object):
    def __init__(self):
        self.current_max = 0
    def maxPathSum(self, root):
        self.dp(root)
        return self.current_max
    def dp(self, root):
        if root==None:
            return 0
        left = self.dp(root.left)
        right = self.dp(root.right)
        if not left or left < 0:
            left = 0
        if not right or right < 0:
            right = 0
        self.current_max = max(left+right+root.val, self.current_max)
        return max(left,right)+root.val
