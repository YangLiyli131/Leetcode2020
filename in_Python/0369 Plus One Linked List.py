# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self, head):
        pre = None
        cur = head
        nex = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = self.rev(head)
        c = 1
        nh = newhead
        while nh:
            tmp = nh.val + c 
            remain = tmp % 10
            c = tmp / 10
            nh.val = remain
            nh = nh.next
        res = self.rev(newhead)
        if c == 1:
            node = ListNode(1)
            node.next = res
            return node
        return res