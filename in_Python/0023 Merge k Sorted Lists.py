# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        tail.next = h1 or h2
        return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        m = len(lists) / 2
        return self.merge(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))
        