class Solution:
  def hIndex(self, citations):
    n = len(citations)
    citations.sort()
    for i, citation in enumerate(citations):
      if citation >= n - i:
        return n - i

    return 0