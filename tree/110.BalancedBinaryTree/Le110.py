#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def deep(self, root):
        if root == None:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        return max(left,right)+1
    def isBalanced(self, root):
        if root == None:
            return True
        if abs(self.deep(root.left)-self.deep(root.right))<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
