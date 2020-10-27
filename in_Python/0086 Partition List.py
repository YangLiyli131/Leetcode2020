# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        d1 = ListNode(0)
        d2 = ListNode(0)
        dd1 = d1
        dd2 = d2
        while head != None:
            if head.val < x:
                d1.next = ListNode(head.val)
                d1 = d1.next
            else:
                d2.next = ListNode(head.val)
                d2 = d2.next
            head = head.next
        d1.next = dd2.next
        return dd1.next