#!/usr/bin/env python
# coding=utf-8
class Graph(object):
    def __init__(self):
        self.node_neighbors={}
        self.visited={}
    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)
    def add_node(self, node):
        if not node in self.node_neighbors:
            self.node_neighbors
