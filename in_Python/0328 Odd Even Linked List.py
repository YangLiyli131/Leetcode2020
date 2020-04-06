# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1 = head
        if head == None: return head
        if head.next == None: return head
        h2 = head.next
        d1 = ListNode(0)
        d1.next = h1
        d2 = ListNode(0)
        d2.next = h2
        while h1 != None and h1.next != None and h1.next.next != None:            
            h1.next = h1.next.next
            h1 = h1.next
            if h1 != None:
                h2.next = h1.next
                h2 = h2.next
        h1.next = d2.next
        return d1.next