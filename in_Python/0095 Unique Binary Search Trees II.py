# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hlp(self, i, j):     
        if i == j:
            return None
        res = []
        for idx in range(i,j):
            for l in self.hlp(i,idx) or [None]:
                for r in self.hlp(idx+1,j) or [None]:
                    ro = TreeNode(idx)
                    ro.left = l
                    ro.right = r
                    res.append(ro)
        return res
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        return self.hlp(1,n+1)
                