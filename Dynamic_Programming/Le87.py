class Solution(object):
    def isScramble(self, s1, s2):
        l = len(s1)
        table = [[[0 for i in range(l+1)] for j in range(l)] for z in range(l)]
        for i in range(l)[::-1]:
            for j in range(l)[::-1]:
                d = min(l-i,l-j)
                for k in range(1,d+1):
                    if s1[i:i+k] == s2[j:j+k]:
                        table[i][j][k] = 1
                    else:
                        for z in range(1, k):
                            if (table[i][j][z] and table[i+z][j+z][k-z]) or (table[i+z][j][k-z] and table[i][j+k-z][z]):
                                table[i][j][k] = 1
                                break
        if table[0][0][l] == 1:
            return True
        else:
            return False