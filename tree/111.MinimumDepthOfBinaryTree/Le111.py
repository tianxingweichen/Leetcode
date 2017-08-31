class Solution(object):
    def front_recursive(self, root, depth, mins):
        if root.left==None and root.right==None:
            if depth < mins:
                mins = depth
                return mins
        if root.left:
            mins = self.front_recursive(root.left, depth+1, mins)
        if root.right:
            mins = self.front_recursive(root.right, depth+1, mins)
        return mins
    def minDepth(self, root):
        if root==None:
            return 0
        else:
            return self.front_recursive(root,1,10000)    
