# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or root.left == None:
            return root
        L = root.left
        R = root.right
        res = self.upsideDownBinaryTree(L)
        L.right = root
        L.left = R
        root.left = None
        root.right = None
        return res
        