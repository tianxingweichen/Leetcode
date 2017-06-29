class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length < 2:
            return 0
        f1 = []
        f2 = []
        mins = prices[0]
        p=0
        for i in range(length):
            mins = min(mins, prices[i])
            p = max(p,prices[i]-mins) 
            f1.append(p)
        maxs = prices[length-1]
        p=0
        for i in range(length)[::-1]:
            maxs = max(maxs,prices[i])
            p = max(p,maxs-prices[i])
            f2.append(p)
        maxp = 0
        for i in range(length):
            q = f1[i] +f2[length-i-1]
            print(q)
            maxp = max(maxp,q)
        return maxp

        