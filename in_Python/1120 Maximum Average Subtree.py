# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res = 0
        def dfs(n):
            if not n:
                return [0,0]
            v = n.val
            cu = 1
            [a,b] = dfs(n.left)
            [c,d] = dfs(n.right)
            v += a + c
            cu += b + d
            self.res = max(self.res, v / float(cu))
            return [v,cu]
        dfs(root)
        return self.res
        