# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root == None:
            return 0
        q = []
        q.append(root)
        while len(q) != 0:
            n = len(q)
            for i in range(n):
                h = q.pop(0)
                if h.left != None:
                    if h.left.left == None and h.left.right == None:
                        res += h.left.val
                    q.append(h.left)
                if h.right != None:
                    q.append(h.right)
        return res