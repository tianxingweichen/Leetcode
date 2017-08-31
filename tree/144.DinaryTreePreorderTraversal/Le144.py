class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return None
        d = []
        myStack = []
        node = root
        myStack.append(node)
        while node or myStack:
            while node:
                d.append(node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            node = node.righCt
