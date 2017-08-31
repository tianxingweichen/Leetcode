class Solution(object):
    def front_recursive(self, root, sum, num):
        num += root.val
        if root.left==None and root.right==None:
            if num == sum:
                num = 0
                return True
        if root.left:
            s = self.front_recursive(root.left,sum, num)
            if s:
                return True
        if root.right:
            s = self.front_recursive(root.right,sum, num)
            if s:
                return True
        return False

    def hasPathSum(self, root, sum):
        if root == None:
            return False
        else:
            return self.front_recursive(root, sum, 0) 
