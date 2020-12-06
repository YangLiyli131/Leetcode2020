"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        l1 = set()
        while p:
            l1.add(p.val)
            p = p.parent
        while q:
            if q.val in l1:
                return q
            q = q.parent
        return p
        