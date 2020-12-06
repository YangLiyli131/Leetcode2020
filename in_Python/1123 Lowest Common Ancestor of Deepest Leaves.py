# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = collections.deque()
        q.append(root)
        x = []
        while q:
            n = len(q)
            cur = []
            while n != 0:
                n -= 1
                h = q.popleft()
                cur.append(h)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
            x = cur
        if len(x) == 1:
            return x[0]
        nodes = set(x)
        def solve(x):
            if not x:
                return x
            if x in nodes:
                return x
            l = solve(x.left)
            r = solve(x.right)
            if l and r:
                return x
            if l:
                return l
            if r:
                return r
        return solve(root)