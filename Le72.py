class Solution(object):
  def minDistance(self, word1, word2):
    l1 = len(word1)
    l2 = len(word2)
    if l1==0 and l2==0:
      return 0
    D = [[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(l1+1):
      D[i][0] = i
    for j in range(l2+1):
      D[0][j] = j
    for i in range(1,l1+1):
      for j in range(1,l2+1):
        if word1[i-1]==word2[j-1]:
          D[i][j] = D[i-1][j-1]
        else:
          D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1])+1

    return D[l1][l2]