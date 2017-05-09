class Solution(object):
    def plusOne(self, digits):
        l = len(digits)
        out = []
        p = 1
        for i in range(l)[::-1]:
            y = digits[i] + p
            if y==10:
                out.append(0)
                p = 1
            else:
                out.append(y)
                p = 0
        if p==1:
            out.append(1)
        out.reverse()
        return out