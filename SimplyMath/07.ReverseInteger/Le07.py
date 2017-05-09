class Solution(object):
    def reverse(self, x):
        y = 0
        if x < 0:
            temp = -1
            x = -1*x
        else:
            temp = 1
        while x != 0:
            d = x % 10
            y = y*10+d
            x = x / 10
        y = y * temp
        if y > 2147483647 or y < -2147483647:
            return 0
        return y