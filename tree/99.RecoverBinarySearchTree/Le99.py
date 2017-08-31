#!/usr/bin/env python
# coding=utf-8
#解题思路：算法一：思路很简单，一颗二叉查找树的中序遍历应该是升序的，而两个节点被交换了，
#那么对这个错误的二叉查找树中序遍历，肯定不是升序的。那我们只需把顺序恢复过来然后进行重新赋值就可以了。
#开辟两个列表，list用来存储被破坏的二叉查找树的节点值，listp用来存储二叉查找树的节点的指针。然后将list排序，再使用listp里面存储的节点指针赋值就可以了。
class Solution(object):
    def __init__(self):
        self.list = []
        self.listp = []
    def inorder_recursive(self, root):
        if root == None:
            return
        self.inorder_recursive(root.left)
        self.list.append(root.val)
        self.listp.append(root)
        self.inorder_recursive(root.right)
    def recoverTree(self, root):
        self.inorder_recursive(root)
        self.list.sort()
        for i in range(len(self.list)):
            self.listp[i].val = self.list[i]
