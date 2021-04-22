# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        h = head
        while h:
            arr.append(h.val)
            h = h.next
        d = collections.Counter(arr)
        p = ListNode(0)
        pp = p
        x = []
        for i in arr:
            if d[i] == 1:
                x.append(i)
        if len(x) == 0:
            return p.next
        h = ListNode(x[0])
        p.next = h
        p = p.next
        for i in x[1:]:
            n = ListNode(i)
            p.next = n
            p = p.next 
        return pp.next
        