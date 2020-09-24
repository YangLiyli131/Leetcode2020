# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head
        
        h = head
        l = 0
        while h != None:
            h = h.next
            l += 1
        if l == 1:
            return head
        k = k % l
        if k == 0:
            return head
        steps = l - k
        h1 = head
        prev = ListNode(0)
        prev.next = h1
        while steps != 0:
            prev = h1
            h1 = h1.next
            steps -= 1
        prev.next = None
        newhead = h1
        h2 = newhead
        while h2 != None and h2.next != None:
            h2 = h2.next
        if h2 != None:
            h2.next = head
        return newhead