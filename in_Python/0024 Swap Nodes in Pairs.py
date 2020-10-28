# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p1 = head
        p2 = head.next
        if p2 == None:
            return head
        h1 = p1
        h2 = p2
        while p1 != None and p1.next != None:
            p1.next = p1.next.next
            p1 = p1.next
            if p1 == None:
                break
            p2.next = p1.next
            p2 = p2.next
        nh = ListNode(0)
        res = nh
        while h1 != None and h2 != None:
            nh.next = h2
            h2 = h2.next
            nh = nh.next
            nh.next = h1
            h1 = h1.next
            nh = nh.next
        nh.next = h1
        return res.next