class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        d = []
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            d.append(node.val)
            node = node.right 
        return d
