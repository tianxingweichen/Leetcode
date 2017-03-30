class Solution(object):
    def isInterleave(self, s1, s2, s3):
        l = len(s3)
        l1 = len(s1)
        l2 = len(s2)
        if l != l1 + l2:
            return False
        table = [[0 for i in range(l2+1)] for j in range(l1+1)]
        table[0][0] = 1
        for i in range(1,l1+1):
            if table[i-1][0] == 1 and s1[i-1] ==s3[i-1]:
                table[i][0] = 1
            else:
                break
        for j in range(1,l2+1):
            if table[0][j-1] == 1 and s2[j-1] == s3[j-1]:
                table[0][j] = 1
            else:
                break
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if table[i][j-1] == 1 and s2[j-1] == s3[i+j-1]:
                    table[i][j] = 1
                if table[i-1][j] == 1 and s1[i-1] == s3[i+j-1]:
                    table[i][j] = 1
        if table[l1][l2]==1:
            return True
        else:
            return False