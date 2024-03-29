# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        nextn = None
        while cur != None:
            nextn = cur.next
            cur.next = pre
            pre = cur
            cur = nextn
        return pre
        