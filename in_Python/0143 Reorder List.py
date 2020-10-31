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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        h2 = self.rev(h2)
        slow.next = None
        nh = TreeNode(0)
        d = nh
        while h2 != None:
            d.next = head
            head = head.next
            d = d.next
            d.next = h2
            h2 = h2.next
            d = d.next
        d.next = head
        return nh.next