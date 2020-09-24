# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return root
        q = []
        q.append(root)
        res = []
        while len(q) != 0:
            cursum = 0
            curcount = len(q)
            n = len(q)
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    q.append(h.left)
                if h.right != None:
                    q.append(h.right)
                cursum += h.val
            res.append(cursum / float(n))
        return res
            