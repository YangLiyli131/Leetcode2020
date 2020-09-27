"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        st = []
        st.append(root)
        while len(st) != 0:
            h = st.pop()
            res.append(h.val)
            t = []
            for ch in h.children:
                t.insert(0,ch)
            for tt in t:
                st.append(tt)
        return res