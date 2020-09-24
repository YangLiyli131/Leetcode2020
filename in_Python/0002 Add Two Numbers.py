# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nhead = ListNode(0)
        h = nhead
        c = 0
        while l1 != None or l2 != None:
            if l1 != None:
                a = l1.val
            else: 
                a = 0
            if l2 != None:
                b = l2.val
            else:
                b = 0
            d = a + b + c
            curnode = ListNode(d % 10)
            nhead.next = curnode
            nhead = curnode
            c = d / 10
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if c == 1:
            nhead.next = ListNode(1)
        return h.next
        