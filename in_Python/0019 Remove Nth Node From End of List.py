# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h1 = head
        h2 = head
        pre = ListNode(0)
        pre.next = head
        while n != 0:
            h2 = h2.next
            n -= 1
        if h2 == None:
            return pre.next.next
        while h2.next != None:
            h1 = h1.next
            h2 = h2.next
        h1.next = h1.next.next
        return head
        