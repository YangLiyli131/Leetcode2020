# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = 0
        lb = 0
        h1 = headA
        h2 = headB
        while h1 != None:
            h1 = h1.next
            la += 1
        while h2 != None:
            h2 = h2.next
            lb += 1
        d = la - lb
        if d > 0:
            while d != 0:
                headA = headA.next
                d -= 1
        else:
            while d != 0:
                headB = headB.next
                d += 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA