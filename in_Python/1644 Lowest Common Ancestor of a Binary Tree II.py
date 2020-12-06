# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root : None}
        dq = collections.deque()
        dq.append(root)
        while dq:
            n = len(dq)
            while n != 0:
                n -= 1
                h = dq.popleft()
                if h.left:
                    dq.append(h.left)
                    parent[h.left] = h
                if h.right:
                    dq.append(h.right)
                    parent[h.right] = h
        if p not in parent or q not in parent:
            return None
        x = set()
        while p:
            x.add(p.val)
            p = parent[p]
        while q:
            if q.val in x:
                return q
            q = parent[q]
        return None