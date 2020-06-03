# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        h = head.next
        p = head
        while h != None:
            if h.val == p.val:
                h = h.next
                p.next = h
            else:
                p = h
                h = h.next
        return head
        