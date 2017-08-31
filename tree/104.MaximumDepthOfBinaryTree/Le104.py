class Solution(object):
    def front_recursive(self, root, depth, maxs):
        if root.left == None and root.right==None:
            if depth > maxs:
                maxs = depth
                return maxs
        if root.left:
            maxs = self.front_recursive(root.left, depth+1, maxs)
        if root.right:
            maxs = self.front_recursive(root.right,depth+1, maxs)
        return maxs
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return self.front_recursive(root, 1, 0)
