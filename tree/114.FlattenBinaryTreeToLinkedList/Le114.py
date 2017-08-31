#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def __init__(self):
        self.listp = []
    def pre_recursive(self, root):
        if root == None:
            return
        self.listp.append(root)
        self.pre_recursive(root.left)
        self.pre_recursive(root.right)
    def flatten(self, root):
        self.pre_recursive(root)
        for i in range(1,len(self.listp)):
            self.listp[i-1].left = None
            self.listp[i-1].right = self.listp[i]



