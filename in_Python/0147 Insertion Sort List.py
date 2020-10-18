# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(1, len(arr)):
            cur = arr[i]
            j = i-1
            while j >= 0 and arr[j] > cur:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = cur
        d = head = ListNode(0)
        for i in arr:
            nn = ListNode(i)
            head.next = nn
            head = head.next
        return d.next