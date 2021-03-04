# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        r = root
        n = 0
        while r:
            n += 1
            r = r.next
        L = n / k
        res = []
        first = n % k
        idx = 0
        Lf = L + 1
        count = 1
        r = root
        while r:
            if first != 0 and count == Lf:
                tmp = r.next
                r.next = None
                res.append(root)
                root = tmp
                count = 0
                first -= 1
                r = root
                count += 1
            elif first == 0 and count == L:
                tmp = r.next
                r.next = None
                res.append(root)
                count = 0
                root = tmp 
                r = root
                count += 1
            else:
                r = r.next
                count += 1
        df = len(res) - k
        while df < 0:
            df += 1
            res.append(None)
        return res