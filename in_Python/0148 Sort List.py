# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        tail.next = h1 or h2
        return dummy.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p,s,f = None, head, head
        while f and f.next:
            p = s
            s = s.next
            f = f.next.next
        p.next = None
        return self.merge(self.sortList(head), self.sortList(s))
        