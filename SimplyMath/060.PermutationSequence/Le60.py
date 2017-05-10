class Solution(object):
    def getPermutation(self, n, k):
        s = [str(i) for i in range(1,n+1)]
        seq = []
        for i in range(n):
            d = 1
            for z in range(1,n-i):
                d = d * z
            print(d)
            j = 1
            while k>(d*j):
                j = j + 1
            k = k - d*(j-1)
            seq.append(s[j-1])
            s.remove(s[j-1])
        se = "".join(seq)
        return se
             