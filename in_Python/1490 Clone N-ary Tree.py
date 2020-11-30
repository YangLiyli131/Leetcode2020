"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        d = {root : Node(root.val)}
        q = collections.deque([root])
        while q:
            h = q.popleft()
            for c in h.children:
                if c not in d:
                    d[c] = Node(c.val)
                    q.append(c)
                d[h].children.append(d[c])
        return d[root]