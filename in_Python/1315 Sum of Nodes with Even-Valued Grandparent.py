# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root == None:
            return 0
        if root.val % 2 == 0:
            if root.left != None:
                if root.left.left != None:
                    res += root.left.left.val
                if root.left.right != None:
                    res += root.left.right.val
            if root.right != None:
                if root.right.left != None:
                    res += root.right.left.val
                if root.right.right != None:
                    res += root.right.right.val
        return res + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
