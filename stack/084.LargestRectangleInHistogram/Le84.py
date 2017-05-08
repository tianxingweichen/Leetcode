class Solution(object):
    def largestRectangleArea(self, heights):
        l = len(heights)
        if l == 0:
            return 0
        stack = []
        stack.append(heights[0])
        _max = stack[-1]
        for i in range(1,l):
            if heights[i]>= stack[-1]:
                stack.append(heights[i])
            else:
                t = 1
                while len(stack)>0 and heights[i]<stack[-1]:
                    p = stack.pop()
                    print(p)
                    area = p * t 
                    _max = max(_max,area)
                    t += 1
                for j in range(t):
                    stack.append(heights[i])      
        for i in range(l):
            area = (l-i)*stack[i]
            _max = max(_max,area)
        return _max