# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        L = 0
        while dummy != None:
            dummy = dummy.next
            L += 1
        i = head
        j = head
        while j != None and j.next != None:
            i = i.next
            j = j.next.next
        return i