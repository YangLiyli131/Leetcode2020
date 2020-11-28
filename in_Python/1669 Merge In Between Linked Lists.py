# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        d = b - a
        pre = ListNode(0)
        l1 = list1
        pre.next = list1
        while a != 0:
            pre = pre.next
            list1 = list1.next
            a -= 1
        nex = list1.next
        while d != 0:
            nex = nex.next
            d -= 1
        pre.next = list2
        l2 = list2
        while l2.next != None:
            l2 = l2.next
        l2.next = nex
        return l1
            
            