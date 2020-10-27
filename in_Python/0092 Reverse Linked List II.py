# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self, h):
        pre = None
        cur = h
        nex = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        pp = pre
        front = head
        tail = head
        nn = n
        mm = m
        while m != 1:
            m -= 1
            pp = pp.next
            front = front.next
        while n != 1:
            n -= 1
            tail = tail.next
        follow = tail.next
        tail.next = None
        prev = self.rev(front)
        pp.next = prev
        nh = prev
        d = nn - mm
        while d != 0:
            d -= 1
            nh = nh.next
        nh.next = follow
        return pre.next