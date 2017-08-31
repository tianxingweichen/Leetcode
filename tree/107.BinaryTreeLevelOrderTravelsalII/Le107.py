#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def pre_recursive(self, root, level, lists):
        if root==None:
            return 
        if len(lists) < level+1:
            lists.append([])
        lists[level].append(root.val)
        self.pre_recursive(root.left, level+1, lists)
        self.pre_recursive(root.right, level+1, lists)
        return lists
    def levelOrderBottom(self, root):
        if root == None:
            return []
        lists = self.pre_recursive(root, 0, [])
        lists.reverse()
        return lists

