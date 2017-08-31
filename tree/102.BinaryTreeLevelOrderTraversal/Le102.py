class Solution(object):
    def __init__(self):
        self.layer = []
    def levelOrder(self, root):
        if root == None:
            return []
        myQueue = []
        lists = []
        l = [root.val]
        myQueue.append(root)
        self.layer.append(0)
        last_layer = -1
        flag = 0
        while myQueue:
            node = myQueue.pop(0)
            current_layer = self.layer.pop(0)
            if current_layer != last_layer:
                lists.append(l)
                l = []
                l.append(node.val)
            else:
                l.append(node.val)
            last_layer = current_layer
            if node.left:
                myQueue.append(node.left)
                self.layer.append(current_layer+1)
            if node.right:
                myQueue.append(node.right)
                self.layer.append(current_layer+1)
        lists.append(l)
        lists.pop(0)
        return lists
＃解题思路：采用dfs，先序遍历的方法，采用一个level值来记录高度，注意要适时扩充list的size
class Solution(object):
    def __init__(self):
        self.lists = []
    def pre_recursive(self, root, level, lists):
        if root == None:
            return
        if len(lists) < level+1:
            lists.append([])
        lists[level].append(root.val)
        self.pre_recursive(root.left, level+1, lists)
        self.pre_recursive(root.right, level+1, lists)
        return lists
    def levelOrder(self,root):
        if root == None:
            return []
        lists = self.pre_recursive(root, 0, [])
        return lists
