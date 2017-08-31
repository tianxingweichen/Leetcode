class Solution(object):
    def front_recursive(self, root, num):
        num = num*10 + root.val
        if root.left == None and root.right ==None:
            return num
        sums = 0
        if root.left:
            sums += self.front_recursive(root.left,num)
        if root.right:
            sums += self.front_recursive(root.right,num)
        return sums
    def sumNumbers(self, root):
        if root == None:
            return 0
        else:
            return self.front_recursive(root)
