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
        d = {}
        qq = [root]
        while qq:
            n = len(qq)
            while n != 0:
                n -= 1
                h = qq.pop(0)
                if h.left:
                    qq.append(h.left)
                    d[h.left] = h
                if h.right:
                    qq.append(h.right)
                    d[h.right] = h
        L1 = [p]
        L2 = [q]
        while L1[-1] in d:
            L1.append(d[L1[-1]])
        while L2[-1] in d:
            L2.append(d[L2[-1]])
        ss = set()
        for x in L1:
            ss.add(x.val)
        for x in L2:
            if x.val in ss:
                return x
        return None