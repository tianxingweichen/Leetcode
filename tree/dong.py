#coding=utf-8
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
class Tree(object):
    def __init__(self):
        self.root = Node()
    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            root = node
        else:
            myQueue = []
            treeNode = node
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if node.lchild == None:
                    treeNode.lchild = node
                    return
                elif node.rchild == None:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)
    def front_recursive(self, root):
        if root == None:
            return 
        print(root.elem)
        self.front_recursive(node.lchild)
        self.front_recursive(node.rchild)
    def front_stack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        myStack.append(node)
        while node or myStack:
            while node:
                print(node.elem)
                myStack.append(node.lchild)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild
    def middle_stack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        myStack.append(node)
        while node or myStack:
            while node:
                myStack.append(node.lchild)
                node = node.lchild
            node = myStack.pop()
            print(node.elem)
            node = node.rchild
    def later_stack(self, root):
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            print(myStack2.pop().elem)
    def level_queue(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild:
                myQueue.append(node.lchild)
            if node.rchild:
                myQueue.append(node.rchild)
















             
        











            

























