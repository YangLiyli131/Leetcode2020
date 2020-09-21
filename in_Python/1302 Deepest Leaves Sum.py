# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        q = []
        if root == None:
            return 0
        q.append(root)
        while len(q) != 0:
            n = len(q)
            rowsum = 0
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    q.append(h.left)
                if h.right != None:
                    q.append(h.right)
                rowsum += h.val
            res.append(rowsum)
        return res[-1]