"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        d = Node(0, None, None)
        pre = d
        st = []
        n = root
        while st or n:
            while n:
                st.append(n)
                n = n.left
            x = st.pop()
            x.left, pre.right, pre = pre, x, x
            n = x.right
        d.right.left, pre.right = pre, d.right
        return d.right