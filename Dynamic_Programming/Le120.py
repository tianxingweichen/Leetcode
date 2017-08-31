class Solution(object):
  def minimumTotal(self, triangle):
    n = len(triangle)
    s = []
    s.append(triangle[0])
    for i in range(1,n):
      m = len(triangle[i])
      t = []
      t.append(triangle[i][0] + s[i-1][0])
      for j in range(1,m-1):
        t.append(triangle[i][j] + min(s[i-1][j-1],s[i-1][j]))
      t.append(triangle[i][m-1] + s[i-1][m-2])
      s.append(t)
    return min(s[n-1]) 
