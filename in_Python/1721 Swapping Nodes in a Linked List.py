# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        arr = []
        headd = head
        while headd:
            arr.append(headd.val)
            headd = headd.next
        tmp = arr[k-1]
        arr[k-1] = arr[len(arr) - k]
        arr[len(arr) - k] = tmp
        pre = ListNode(0)
        h = ListNode(arr[0])
        pre.next = h
        for x in arr[1:]:
            h.next = ListNode(x)
            h = h.next 
        return pre.next