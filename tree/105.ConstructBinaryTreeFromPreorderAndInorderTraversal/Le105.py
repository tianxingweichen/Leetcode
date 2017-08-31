class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        root = self._buildTree(0, len(preorder), 0, len(inorder))
        return root
    def _buildTree(self, prestart, preend, instart, inend):
        if prestart >= preend:
            return None
        root = TreeNode(self.preorder[prestart])
        offset = self.inorder[instart:inend].index(root.val)
        root.left = self._buildTree(prestart+1, prestart+offset+1, instart, instart+offset+1)
        root.right = self._buildTree(prestart+offset+1, preend, instart+offset+1, inend)
        return root
