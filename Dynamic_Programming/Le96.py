class Solution(object):
    def numTrees(self, n):
        trees = [0 for i in range(n+1)]
        trees[0] = 1 
        trees[1] = 1
        if n == 1:
            return trees[n]
        for i in range(2,n+1):
            trees[i] = 0
            for j in range(i):
                trees[i] = trees[i] + trees[j]*trees[i-j-1]
        return trees[n]