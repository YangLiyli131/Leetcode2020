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
    def flipBinaryTree(self, root, leaf):
        """
        :type node: Node
        :rtype: Node
        """
        cur = leaf
        p = None
        while cur:
            if cur.left:
                if cur != root:
                    cur.right = cur.left
                else:
                    cur.parent = p
                    break
            if cur.parent and cur.parent.left == cur:
                cur.parent.left = None
            if cur.parent and cur.parent.right == cur:
                cur.parent.right = None
            tmp = cur.parent 
            cur.left = cur.parent 
            cur.parent = p
            p = cur
            cur = tmp
        return leaf
                