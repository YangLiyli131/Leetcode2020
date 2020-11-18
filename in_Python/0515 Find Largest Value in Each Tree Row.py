# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        q = [root]
        while q:
            n = len(q)
            curmax = -sys.maxint
            while n != 0:
                n -= 1
                h = q.pop(0)
                curmax = max(curmax, h.val)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
            res.append(curmax)
        return res