"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        all_children = set()
        for x in tree:
            for xh in x.children:
                all_children.add(xh)
        for x in tree:
            if x not in all_children:
                return x
        return None