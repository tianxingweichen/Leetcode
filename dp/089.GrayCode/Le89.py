#!/usr/bin/env python
# coding=utf-8
import sys 
class Solution(object):
    def grayCode(self, n):
        _list = [0]
        for i in range(n):
            length = len(_list)
            for j in range(length)[::-1]:
                d = _list[j] + 2**i
                _list.append(d)
        return _list

sol = Solution()
n = sys.stdin.readline().strip()
n = int(n)
lists = sol.grayCode(n)
print(lists)




