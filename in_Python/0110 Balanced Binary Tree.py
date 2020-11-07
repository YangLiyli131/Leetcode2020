# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, n):
        if n == None:
            return 0
        if not n.left and not n.right:
            return 1 
        return 1 + max(self.height(n.left), self.height(n.right))
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if not root.left and not root.right:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)