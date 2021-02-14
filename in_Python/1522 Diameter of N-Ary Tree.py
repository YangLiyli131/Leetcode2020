"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            tmp = []
            for x in root.children:
                tmp.append(dfs(x))
            tmp.sort(reverse = True)
            if tmp:
                self.res = max(self.res, tmp[0] + tmp[1] if len(tmp) > 1 else tmp[0])
                return 1 + max(tmp)
            else:
                return 1
        dfs(root)
        return self.res