class Solution:
  def rotateRight(self, head, k): 
    if not head or not head.next or k == 0:
      return head
    tail = head
    length = 1
    while tail.next:
      tail = tail.next
      length += 1
    tail.next = head  
    t = length - k % length
    for _ in range(t):
      tail = tail.next
    newHead = tail.next
    tail.next = None
    return newHead