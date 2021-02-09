# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        if root.val > V:
            l, r = self.splitBST(root.left, V)
            root.left = r
            return [l,root]
        else:
            l, r = self.splitBST(root.right, V)
            root.right = l
            return [root,r]
    
        