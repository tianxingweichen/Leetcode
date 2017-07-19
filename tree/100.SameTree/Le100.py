class Solution(object):
    def front_recursive(self, root):
        if root == None:
            return None
        d = []
        d.append(root.val)
        self.front_recursive(root.left)
        self.front_recursive(root.right)
        return d
    def isSameTree(self, p, q):
        d1 = self.front_recursive(p)
        d2 = self.front_recursive(q)
        if d1 == d2:
            return True
        else:
            return False
