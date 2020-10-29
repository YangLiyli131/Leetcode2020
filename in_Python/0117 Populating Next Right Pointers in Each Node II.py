"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return root
        q = [root]
        while q:
            n = len(q)
            pre = None
            while n != 0:
                n -= 1
                h = q.pop(0)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
                if pre:
                    pre.next = h
                pre = h
        return root