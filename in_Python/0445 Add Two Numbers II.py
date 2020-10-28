# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        b = 0
        h1 = l1
        h2 = l2
        while h1 != None:
            a = a * 10 + h1.val
            h1 = h1.next
        while h2 != None:
            b = b * 10 + h2.val
            h2 = h2.next
        r = str(a+b)
        h = ListNode(0)
        rr = h
        for s in r:
            h.next = ListNode(int(s))
            h = h.next
        return rr.next