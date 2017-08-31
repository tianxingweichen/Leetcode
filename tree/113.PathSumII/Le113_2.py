#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def __init__(self):
        self.lists = []
    def Sum(self, root, sum):
        if root == None:
            return []
        l = []
        if root.val==sum and root.left==None and root.right==None:
            l.append(root.val)
        else:
            l = None
        self.lists.append(l)
        left = self.pathSum(root.left, sum-root.val)
        if left != None:
            left = left+[root.val]
            self.lists.append(left)
        right = self.pathSum(root.right, sum-root.val)
        if right != None:
            right = right+[root.val]
            self.lists.append(right)
        return l
    def pathSum(self, root, sum):
        if root == None:
            return []
        self.Sum(root, sum)
        return self.lists


            
