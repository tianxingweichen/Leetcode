class Solution(object):
    def maxProfit(self, prices):
        l = len(prices)
        if l == 0:
            return 0
        profit = [0 for i in range(l)]
        minbuy = prices[0]
        for i in range(1,l):
            if prices[i] < minbuy:
                minbuy = prices[i]
            else:
                profit[i] = prices[i] - minbuy
        return max(profit)