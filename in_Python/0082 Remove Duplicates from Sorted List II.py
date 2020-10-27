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
        p = ListNode(0)
        pp = p
        p.next = head
        cur = head
        nex = head.next
        if nex == None:
            return head
        while nex != None:
            nex = cur.next
            f = 0
            while nex != None and nex.val == cur.val:
                f = 1
                nex = nex.next
            if f == 0:
                p = cur
                cur = nex
            else:
                cur = nex                
                p.next = cur
        return pp.next
        
        