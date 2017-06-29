class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        for i in range(lt):
            if lt[i] not in s:
                return ""
        i = 0
        while i < ls:
           q = t
           if ls[i] in q:
               i = i + 1
                