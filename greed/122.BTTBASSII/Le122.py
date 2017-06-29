class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length < 2:
            return 0
        mins = prices[0]
        i = 0
        p = 0
        while i < length:
            while i<length and prices[i] <= mins:
                mins = prices[i] 
                i = i + 1
            maxs = mins
            while  i<length and prices[i] >= maxs:
                maxs = prices[i]
                i = i + 1
            p = p + maxs-mins
            if i < length:
                mins = prices[i]
        return p