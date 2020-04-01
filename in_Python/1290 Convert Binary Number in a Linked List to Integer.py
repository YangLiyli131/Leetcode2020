# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = []
        while head != None:
            temp.insert(0,head.val)
            head = head.next
        res = 0
        for i in range(len(temp)):
            res += temp[i] * (2 ** i)
        return res
        