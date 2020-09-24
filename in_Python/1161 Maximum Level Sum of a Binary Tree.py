# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append(root)
        res = []
        maxid = 1
        level = 1
        maxsum = root.val
        while len(q) != 0:
            n = len(q)
            cur = []
            ss = 0
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    q.append(h.left)
                if h.right != None:
                    q.append(h.right)
                cur.append(h.val)
                ss += h.val
            res.append(cur)
            if ss > maxsum:
                maxsum = ss
                maxid = level
            level += 1
        return maxid
        