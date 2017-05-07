class Solution(object):
    def longestValidParentheses(self, s):
        l = len(s)
        stack = []
        mark = []
        maxs = 0
        start = 0
        for i in range(l):
            if s[i]=='(':
                stack.append('(') 
                mark.append(i)
            else:
                if len(stack)==0:
                    start = i + 1
                else:
                    stack.pop()
                    mark.pop()
                    if len(stack)==0:
                        maxs = max(maxs,i - start + 1)
                    else:
                        maxs = max(maxs, i-mark[-1])
        return maxs