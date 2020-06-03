# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = ListNode()
        pre.next = head
        nh = pre
        while head != None:
            if head.val == val:
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next
        return nh.next
        