"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        q = []
        if root == None:
            return q
        q.append(root)
        res = []
        while len(q) != 0:
            n = len(q)
            cur = []
            for i in range(n):
                h = q.pop(0)
                for ch in h.children:
                    q.append(ch)
                cur.append(h.val)
            res.append(cur)
        return res
        