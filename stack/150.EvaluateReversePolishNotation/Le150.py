class Solution(object):
    def isdigits(self,x):
        try:
            int(x)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens):
        stack = []
        l = len(tokens)
        for i in range(l):
            if self.isdigits(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                x1 = stack.pop()
                x2 = stack.pop()
                if tokens[i]=='+':
                    y = x1+x2
                elif tokens[i]=='-':
                    y = x2 - x1
                elif tokens[i]=='*':
                    y = x1 * x2
                else:
                    if x1*x2<0:
                        y = -((-x2)/x1)
                    else:
                        y = x2 / x2
                stack.append(y)
        y = stack.pop()
        return y