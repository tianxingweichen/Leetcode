class Solution(object):
    def __init__(self):
        self.lists = []
    def front_recursive(self, root, sum, num, l):
        if root.left==None and root.right==None:
            if num == sum:
                self.lists.append(l)
        if root.left:
            self.front_recursive(root.left, sum, num+root.left.val, l+[root.left.val])
        if root.right:
            self.front_recursive(root.right, sum,num+root.right.val, l+[root.right.val])
    def pathSum(self, root, sum):
        if root==None:
            return []
        self.front_recursive(root, sum, root.val, [root.val])
        return self.lists
