"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        st = []
        if root == None:
            return res
        st.append(root)
        while len(st) != 0:
            h = st.pop()
            for ch in h.children:
                st.append(ch)
            res.insert(0, h.val)
        return res
        