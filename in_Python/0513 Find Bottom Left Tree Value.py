# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        res = []
        while q:
            n = len(q)
            cur = []
            while n != 0:
                n -= 1
                h = q.pop(0)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
                cur.append(h.val)
            res.append(cur)
        return res[-1][0]
        