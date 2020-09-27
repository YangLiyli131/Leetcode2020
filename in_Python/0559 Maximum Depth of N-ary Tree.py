"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        q = []
        q.append(root)
        res = 0
        while len(q) != 0:
            n = len(q)
            for i in range(n):
                h = q.pop(0)
                if h == None:
                    continue
                for ch in h.children:
                    q.append(ch)
            res += 1
        return res