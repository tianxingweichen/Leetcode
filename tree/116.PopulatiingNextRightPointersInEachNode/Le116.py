#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def __init__(self):
        self.layer = []
    def connect(self, root):
        if root:
            myQueue = []
            myQueue.append(root)
            last_layer = -1
            self.layer.append(0)
            last_node = root
            while myQueue:
                current_node = myQueue.pop(0)
                current_layer = self.layer.pop(0)
                if current_layer==last_layer:
                    last_node.next = current_node
                else:
                    last_node.next = None
                last_layer = current_layer
                last_node = current_node
                if current_node.left:
                    myQueue.append(current_node.left)
                    self.layer.append(current_layer+1)
                if current_node.right:
                    myQueue.append(current_node.right)
                    self.layer.append(current_layer+1)
