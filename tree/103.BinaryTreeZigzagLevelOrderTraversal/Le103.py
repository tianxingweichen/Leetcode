class Solution(object):
    def level_recursive(self, root):
        zig = []
        myQueue = []
        Tdeep = []
        node = root
        myQueue.append(root)
        Tdeep.append(1)
        l = []
        d = 1
        while myQueue:
            node = myQueue.pop(0)
            deep = Tdeep.pop(0)
            if deep==d:
                l.append(node.val)
            else:
                zig.append(l)
                l = []
                l.append(node.val)
                d = deep
            if node.left:
                myQueue.append(node.left)
                Tdeep.append(deep+1) 
            if node.right:
                myQueue.append(node.right)
                Tdeep.append(deep+1)
        zig.append(l)
        return zig
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        zig = self.level_recursive(root)
        for i in range(len(zig)):
            if i % 2 ==1:
                zig[i].reverse()
        return zig
