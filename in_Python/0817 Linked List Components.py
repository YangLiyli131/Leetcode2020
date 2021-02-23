# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        r = 0
        cur = []
        while head:
            v = head.val
            if v not in g:
                if len(cur) != 0:
                    r += 1
                    cur = []
            else:
                cur.append(v)
                g.remove(v)
            head = head.next
        if len(cur) != 0:
            r += 1
        return r