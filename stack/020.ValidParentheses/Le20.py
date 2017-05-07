class Solution(object):
    def isValid(self, s):
        l = len(s)
        if l < 2:
            return False
        stack = []
        for i in range(l):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if s[i]==')':
                        if stack.pop() != '(':
                            return False
                    elif s[i]==']':
                        if stack.pop() != '[':
                            return False
                    else:
                        if stack.pop() != '{':
                            return False
        if len(stack)==0:
            return True
        else:
            return False