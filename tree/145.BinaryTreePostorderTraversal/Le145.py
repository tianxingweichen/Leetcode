class Solution(object):
    def postorderTraversal(self, root):
        if root == None:
            return []
        d = []
        node = root
        myStack1 = []
        myStack2 = []
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:
            d.append(myStack2.pop().val)
        return d
