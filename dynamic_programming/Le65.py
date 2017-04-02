class Solution(object):
    def climbStairs(self, n):
        S = [0 for i in range(n)]
        if n == 1:
            return 1
        S[0] = 1
        S[1] = 2
        for i in range(2,n):
            S[i] = S[i-1] + S[i-2]
        return S[n-1]