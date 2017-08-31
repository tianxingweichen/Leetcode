# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        root = self._buildTree(0, len(postorder), 0, len(inorder))
        return root
    def _buildTree(self, post_start, post_end, in_start, in_end):
        if post_start >= post_end:
            return None
        val = self.postorder[post_end-1]
        root = TreeNode(val)
        offset = self.inorder[in_start:in_end].index(val)
        root.left = self._buildTree(post_start, post_start+offset, in_start, in_start+offset)
        root.right = self._buildTree(post_start+offset, post_end-1, in_start+offset+1, in_end)
        return root
