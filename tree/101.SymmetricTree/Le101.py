class Solution(object):
    def __init__(self):
        self.lists = []
    def sym(self, left, right):
        if left==None and right==None:
            return True
        if left and right and left.val==right.val:
            return self.sym(left.left, right.right) and self.sym(left.right, right.left)
        else:
            return False
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.sym(root.left, root.right)
        
